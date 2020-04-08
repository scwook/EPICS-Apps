#-*- coding:utf-8 -*-
import sys
import time
import serial
import threading

from multiprocessing import Queue
from pvaccess import *

class Protocol(object):
    """\
    Protocol as used by the ReaderThread. This base class provides empty
    implementations of all methods.
    """

    def connection_made(self, transport):
        """Called when reader thread is started"""

    def data_received(self, data):
        """Called with snippets received from the serial port"""

    def connection_lost(self, exc):
        """\
        Called when the serial port is closed or the reader loop terminated
        otherwise.
        """
        if isinstance(exc, Exception):
            raise exc


class ReaderThread(threading.Thread):
    """\
    Implement a serial port read loop and dispatch to a Protocol instance (like
    the asyncio.Protocol) but do it with threads.
    Calls to close() will close the serial port but it is also possible to just
    stop() this thread and continue the serial port instance otherwise.
    """

    def __init__(self, serial_instance, protocol_factory):
        """\
        Initialize thread.
        Note that the serial_instance' timeout is set to one second!
        Other settings are not changed.
        """
        super(ReaderThread, self).__init__()
        self.daemon = True
        self.serial = serial_instance
        self.protocol_factory = protocol_factory
        self.alive = True
        self._lock = threading.Lock()
        self._connection_made = threading.Event()
        self.protocol = None

    def stop(self):
        """Stop the reader thread"""
        self.alive = False
        if hasattr(self.serial, 'cancel_read'):
            self.serial.cancel_read()
        self.join(2)

    def run(self):
        """Reader loop"""
        if not hasattr(self.serial, 'cancel_read'):
            self.serial.timeout = 1
        self.protocol = self.protocol_factory()
        try:
            self.protocol.connection_made(self)
        except Exception as e:
            self.alive = False
            self.protocol.connection_lost(e)
            self._connection_made.set()
            return
        error = None
        self._connection_made.set()
        while self.alive and self.serial.is_open:
            try:
                # read all that is there or wait for one byte (blocking)
                #data = self.serial.read(self.serial.in_waiting or 1)
	        data = self.serial.readline()
		data = data.replace('\n', '')

            except serial.SerialException as e:
                # probably some I/O problem such as disconnected USB serial
                # adapters -> exit
                error = e
                break
            else:
                if data:
                    # make a separated try-except for called used code
                    try:
                    #    self.protocol.data_received(data)
			value = dataDic[str(data)] + '\n'
			print(value)
                        self.write(value)
                    except Exception as e:
                        error = e
                        break
        self.alive = False
        self.protocol.connection_lost(error)
        self.protocol = None

    def write(self, data):
        """Thread safe writing (uses lock)"""
        with self._lock:
            self.serial.write(str(data))

    def close(self):
        """Close the serial port and exit reader thread (uses lock)"""
        # use the lock to let other threads finish writing
        with self._lock:
            # first stop reading, so that closing can be done on idle port
            self.stop()
            self.serial.close()

    def connect(self):
        """
        Wait until connection is set up and return the transport and protocol
        instances.
        """
        if self.alive:
            self._connection_made.wait()
            if not self.alive:
                raise RuntimeError('connection_lost already called')
            return (self, self.protocol)
        else:
            raise RuntimeError('already stopped')

    # - -  context manager, returns protocol

    def __enter__(self):
        """\
        Enter context handler. May raise RuntimeError in case the connection
        could not be created.
        """
        self.start()
        self._connection_made.wait()
        if not self.alive:
            raise RuntimeError('connection_lost already called')
        return self.protocol

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Leave context: close port"""
        self.close()

class rawProtocal(Protocol):
    def connection_made(self, transport):
        self.transport = transport
        self.running = True

    def connection_lost(self, exc):
        self.transport = None

    def data_received(self, data):
        print('Unknown data', data)

    def write(self,data):
        print(data)
        self.transport.write(data)

    def isDone(self):
        return self.running

class ChannelMonitor:
    def __init__(self, name):
        self.name = name

    def monitor(self, data):
        dataDic[self.name] = str(data['value'])

PORT = '/dev/ttyAMA0'
ser = serial.serial_for_url(PORT, baudrate=9600, timeout=3)

pvList = list(line.strip() for line in open('pvList'))

channelList = list()
monitoringList = list()
dataDic = dict()

index = 0
for name in pvList:
	dataDic[name] = "06.19"
        channelList.append(Channel(name, ProviderType.CA))
        monitoringList.append(ChannelMonitor(name))

        channelList[index].monitor(monitoringList[index].monitor)
        index += 1

#pv1 = "scwookHost:ai1"
#pv2 = "scwookHost:ai2"
#pv3 = "scwookHost:ai3"

#dic = {pv1:0.0, pv2:0.0, pv3:0.0}

#c1 = Channel(pv1, ProviderType.CA)
#m1 = ChannelMonitor(pv1)
#c1.monitor(m1.monitor)

#c2 = Channel(pv2, ProviderType.CA)
#m2 = ChannelMonitor(pv2)
#c2.monitor(m2.monitor)

#c3 = Channel(pv3, ProviderType.CA)
#m3 = ChannelMonitor(pv3)
#c3.monitor(m3.monitor)

with ReaderThread(ser, rawProtocal) as p:
    while p.isDone():
        time.sleep(0.1)
