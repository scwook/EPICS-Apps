TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC = bme280
# bme280.dbd will be created and installed
DBD += bme280.dbd

# bme280.dbd will be made up from these files:
bme280_DBD += base.dbd

# Include dbd files from all support applications:
#bme280_DBD += xxx.dbd
#bme280_DBD += asyn.dbd
bme280_DBD += stream.dbd
bme280_DBD += drvAsynIPPort.dbd

# Add all the support libraries needed by this IOC
#bme280_LIBS += xxx
bme280_LIBS += stream
bme280_LIBS += asyn

# bme280_registerRecordDeviceDriver.cpp derives from bme280.dbd
bme280_SRCS += bme280_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
bme280_SRCS_DEFAULT += bme280Main.cpp
bme280_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#bme280_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Finally link to the EPICS Base libraries
bme280_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

