TOP=../..

include $(TOP)/configure/CONFIG
#----------------------------------------
#  ADD MACRO DEFINITIONS AFTER THIS LINE
#=============================

#=============================
# Build the IOC application

PROD_IOC = recExample
# recExample.dbd will be created and installed
DBD += recExample.dbd

# recExample.dbd will be made up from these files:
recExample_DBD += base.dbd

# Include dbd files from all support applications:
#recExample_DBD += xxx.dbd

# Add all the support libraries needed by this IOC
#recExample_LIBS += xxx

# recExample_registerRecordDeviceDriver.cpp derives from recExample.dbd
recExample_SRCS += recExample_registerRecordDeviceDriver.cpp

# Build the main IOC entry point on workstation OSs.
recExample_SRCS_DEFAULT += recExampleMain.cpp
recExample_SRCS_vxWorks += -nil-

# Add support from base/src/vxWorks if needed
#recExample_OBJS_vxWorks += $(EPICS_BASE_BIN)/vxComLibrary

# Finally link to the EPICS Base libraries
recExample_LIBS += $(EPICS_BASE_IOC_LIBS)

#===========================

ifneq ($(SNCSEQ),)
    recExample_DBD += seqRecExample.dbd
    recExample_SRCS += seqBinary.stt
    recExample_SRCS += seqAnalog.stt
    recExample_SRCS += seqWaveform.stt
    recExample_LIBS += seq pv
endif

include $(TOP)/configure/RULES
#----------------------------------------
#  ADD RULES AFTER THIS LINE

