#!/usr/bin/env python3

from subprocess import *

from plistlib import *

import os

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

                if ( os.path.isfile('xml/' + iDev_1 + '.xml') ):
			print("We have this device already")
		else:
			iDev1XML = Popen(["/home/pi/Desktop/code/fearMe/grabDev.sh", iDev_1], shell=False)

                if ( os.path.isfile('xml/' + iDev_2 + '.xml') ):
			print("We have this device already")
		else:
			iDev2XML = Popen(["/home/pi/Desktop/code/fearMe/grabDev.sh", iDev_2], shell=False)

		readDev(iDev_1)
		readDev(iDev_2)

		print('First device specs:' + iDev_1_plist['DeviceName'] + iDev_1_plist['ProductVersion'] + iDev_1_plist['DeviceColor'] + iDev_1_plist['HardwareModel'])
		print('Second device specs:' + iDev_2_plist['DeviceName'] + iDev_2_plist['ProductVersion'] + iDev_2_plist['DeviceColor'] + iDev_2_plist['HardwareModel'])

	else:
		iDev = attached_iDevices[0][2:]

		if ( os.path.isfile('xml/' + iDev + '.xml') ):
			print("We have this device already")
			readDev(iDev)
		else:
			iDevXML = Popen(["/home/pi/Desktop/code/fearMe/grabDev.sh", iDev], shell=False)

def readDev(iDev):
	iDev_plist = readPlist('xml/' + iDev + '.xml')
	print('Device specs:' + iDev_plist['DeviceName'] + iDev_plist['ProductVersion'] + iDev_plist['DeviceColor'] + iDev_plist['HardwareModel'])

if __name__ == "__main__": main()
