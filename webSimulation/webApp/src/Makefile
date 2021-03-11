TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC = web
# web.dbd will be created and installed
DBD += web.dbd

# web.dbd will be made up from these files:
web_DBD += base.dbd

# Include dbd files from all support applications:
#web_DBD += xxx.dbd

# Add all the support libraries needed by this IOC
#web_LIBS += xxx

# web_registerRecordDeviceDriver.cpp derives from web.dbd
web_SRCS += web_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
web_SRCS_DEFAULT += webMain.cpp
web_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#web_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Finally link to the EPICS Base libraries
web_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

