#!../../bin/darwin-x86/web

#- You may have to change web to something else
#- everywhere it appears in this file

< envPaths

cd "${TOP}"

## Register all support components
dbLoadDatabase "dbd/web.dbd"
web_registerRecordDeviceDriver pdbbase

## Load record instances
#dbLoadRecords("db/xxx.db","user=scwook")
dbLoadRecords("db/timing.db" "SYS=WEB,SUBSYS=PAGE,DEV=TIMING,SUBDEV=CHOPPER")
dbLoadRecords("db/timing.db" "SYS=WEB,SUBSYS=PAGE,DEV=TIMING,SUBDEV=RFQ")
dbLoadRecords("db/timing.db" "SYS=WEB,SUBSYS=PAGE,DEV=TIMING,SUBDEV=ACCT")

dbLoadRecords("db/fps.db" "SYS=WEB,SUBSYS=PAGE,DEV=FPS,SUBDEV=NODE1")
dbLoadRecords("db/fps.db" "SYS=WEB,SUBSYS=PAGE,DEV=FPS,SUBDEV=NODE2")
dbLoadRecords("db/fps.db" "SYS=WEB,SUBSYS=PAGE,DEV=FPS,SUBDEV=NODE3")
dbLoadRecords("db/fps.db" "SYS=WEB,SUBSYS=PAGE,DEV=FPS,SUBDEV=NODE4")
dbLoadRecords("db/fps.db" "SYS=WEB,SUBSYS=PAGE,DEV=FPS,SUBDEV=NODE5")
dbLoadRecords("db/fps.db" "SYS=WEB,SUBSYS=PAGE,DEV=FPS,SUBDEV=NODE6")
dbLoadRecords("db/fps.db" "SYS=WEB,SUBSYS=PAGE,DEV=FPS,SUBDEV=NODE7")

cd "${TOP}/iocBoot/${IOC}"
iocInit

## Start any sequence programs
#seq sncxxx,"user=scwook"
