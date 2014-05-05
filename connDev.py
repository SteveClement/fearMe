#!/usr/bin/env python3

from subprocess import *

from plistlib import *

fhCH = open('connectionHistory.txt','a')

output=check_output("/home/pi/Desktop/code/fearMe/grabDev.sh", shell=True)

attached_iDevices = str(check_output(["/usr/bin/idevice_id", "-l"])).rstrip().split('\\n')

if output:
	print(output, file=fhCH)
	fhCH.close()

if attached_iDevices:
	if ( len(attached_iDevices) > 2 ):
		print("More than 1 iDevice detected")
		iDev_1 = attached_iDevices[0][2:]
		iDev_2 = attached_iDevices[1]

		iDev1XML = Popen(["/home/pi/Desktop/code/fearMe/grabDev.sh", iDev_1], shell=False)

		iDev2XML = Popen(["/home/pi/Desktop/code/fearMe/grabDev.sh", iDev_2], shell=False)

		print(iDev_1)
		print(iDev_2)
	else:
		iDev = attached_iDevices[0][2:]
		iDevXML = Popen(["/home/pi/Desktop/code/fearMe/grabDev.sh", iDev], shell=False)
