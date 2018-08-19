#!../../bin/linux-arm/lox02s

## You may have to change lox02s to something else
## everywhere it appears in this file

< envPaths

cd "${TOP}"

epicsEnvSet "STREAM_PROTOCOL_PATH" "../../proto"

## Register all support components
dbLoadDatabase "dbd/lox02s.dbd"
lox02s_registerRecordDeviceDriver pdbbase

drvAsynIPPortConfigure("LOX", "192.168.0.19:23", 0, 0, 0)

## Load record instances
#dbLoadRecords("db/xxx.db","user=piHost")
dbLoadRecords("db/lox02s.db", "P=LOX")

cd "${TOP}/iocBoot/${IOC}"
iocInit

## Start any sequence programs
#seq sncxxx,"user=piHost"
