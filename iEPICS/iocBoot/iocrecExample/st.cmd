#!../../bin/linux-x86_64/recExample

## You may have to change recExample to something else
## everywhere it appears in this file

< envPaths

cd "${TOP}"

## Register all support components
dbLoadDatabase "dbd/recExample.dbd"
recExample_registerRecordDeviceDriver pdbbase

## Load record instances
#dbLoadRecords("db/xxx.db","user=scwookHost")
dbLoadRecords("db/example.db", "SYS=scwook,SUBSYS=iepics,DEV=record,SUBDEV=test")

cd "${TOP}/iocBoot/${IOC}"
iocInit

## Start any sequence programs
#seq sncxxx,"user=scwookHost"
