#!../../bin/linux-arm/client

## You may have to change client to something else
## everywhere it appears in this file

< envPaths

cd "${TOP}"

epicsEnvSet "STREAM_PROTOCOL_PATH" "../../proto"

## Register all support components
dbLoadDatabase "dbd/client.dbd"
client_registerRecordDeviceDriver pdbbase

# Raspberry Pi 2 serial device name is ttyAMA0
# Raspberry Pi 3 serial device name is ttyS0

drvAsynSerialPortConfigure "UART" "/dev/ttyS0"

asynSetOption("UART", 0, "baud", "115200")
asynSetOption("UART", 0, "bits", "8")
asynSetOption("UART", 0, "parity", "none")

## Load record instances
#dbLoadRecords("db/xxx.db","user=ctrluserHost")
#dbLoadRecords("db/ai.db", "pvname=scwookHost")
dbLoadTemplate("db/test.substitutions")

cd "${TOP}/iocBoot/${IOC}"
iocInit

## Start any sequence programs
#seq sncxxx,"user=ctrluserHost"
