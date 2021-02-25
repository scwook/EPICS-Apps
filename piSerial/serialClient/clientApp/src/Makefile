TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC = client
# client.dbd will be created and installed
DBD += client.dbd

# client.dbd will be made up from these files:
client_DBD += base.dbd

# Include dbd files from all support applications:
#client_DBD += xxx.dbd
client_DBD += stream.dbd
client_DBD += asyn.dbd
client_DBD += drvAsynSerialPort.dbd

# Add all the support libraries needed by this IOC
#client_LIBS += xxx
client_LIBS += stream
client_LIBS += asyn

# client_registerRecordDeviceDriver.cpp derives from client.dbd
client_SRCS += client_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
client_SRCS_DEFAULT += clientMain.cpp
client_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#client_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Finally link to the EPICS Base libraries
client_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

