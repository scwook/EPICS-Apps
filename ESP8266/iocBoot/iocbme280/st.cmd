#!../../bin/linux-arm/bme280

## You may have to change bme280 to something else
## everywhere it appears in this file

< envPaths

cd "${TOP}"

epicsEnvSet "STREAM_PROTOCOL_PATH" "../../proto"

## Register all support components
dbLoadDatabase "dbd/bme280.dbd"
bme280_registerRecordDeviceDriver pdbbase

drvAsynIPPortConfigure("ETH", "192.168.0.17:23", 0, 0, 0)

## Load record instances
#dbLoadRecords("db/xxx.db","user=scwookHost")
dbLoadRecords("db/bme280.db")

cd "${TOP}/iocBoot/${IOC}"
iocInit

## Start any sequence programs
#seq sncxxx,"user=scwookHost"
