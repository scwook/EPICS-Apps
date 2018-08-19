TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC = lox02s
# lox02s.dbd will be created and installed
DBD += lox02s.dbd

# lox02s.dbd will be made up from these files:
lox02s_DBD += base.dbd

# Include dbd files from all support applications:
#lox02s_DBD += xxx.dbd
lox02s_DBD += stream.dbd
lox02s_DBD += drvAsynIPPort.dbd

# Add all the support libraries needed by this IOC
#lox02s_LIBS += xxx
lox02s_LIBS += stream
lox02s_LIBS += asyn

# lox02s_registerRecordDeviceDriver.cpp derives from lox02s.dbd
lox02s_SRCS += lox02s_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
lox02s_SRCS_DEFAULT += lox02sMain.cpp
lox02s_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#lox02s_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Finally link to the EPICS Base libraries
lox02s_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

