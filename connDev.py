#!/usr/bin/env python3

from subprocess import *
from plistlib import *
from time import *
from os.path import expanduser
import os



def main():

	setup()
	home = expanduser("~")
	code = "/Desktop/code/fearMe"
	grabDev = home + code + "/grabDev.sh"

	fhCH = open('txt/connectionHistory.txt','a')

	output=check_output(grabDev, shell=True)

	try:
		attached_iDevices = str(check_output(["/usr/bin/idevice_id", "-l"])).rstrip().split('\\n')
		print("Grabbing attached iDevices")
	except:
		print("No iDevice connected, move along")

	if output:
		print(output, file=fhCH)
		attachedDevices=str(output).rstrip().split('\\n')
		print(attachedDevices[0][2:].split(":")[0] + ":" + attachedDevices[0][2:].split(":")[1])
		print(attachedDevices[1].split(":")[0] + ":" + attachedDevices[1].split(":")[1])
		fhCH.close()

	if attached_iDevices:
		if ( len(attached_iDevices) > 2 ):
			print("More than 1 iDevice detected")
			iDev_1 = attached_iDevices[0][2:]
			iDev_2 = attached_iDevices[1]

			if ( os.path.isfile('xml/' + iDev_1 + '.xml') ):
				print("We have this device already")
				readDev(iDev_1)
			else:
				iDev1XML = Popen([grabDev, iDev_1], shell=False)
				readDev(iDev_1)

			if ( os.path.isfile('xml/' + iDev_2 + '.xml') ):
				print("We have this device already")
				readDev(iDev_2)
			else:
				iDev2XML = Popen([grabDev, iDev_2], shell=False)
				readDev(iDev_2)

		else:
			iDev = attached_iDevices[0][2:]

			if ( os.path.isfile('xml/' + iDev + '.xml') ):
				print("We have this device already")
				readDev(iDev)
			else:
				iDevXML = Popen([grabDev, iDev], shell=False)
				readDev(iDev)

def readDev(iDev):
	sleep(2)
	iDev_plist = readPlist('xml/' + iDev + '.xml')
	if iDev_plist['DeviceColor'] == '#3b3b3c':
		iDev_plist['DeviceColor'] = 'grey'
	print('Device specs: {} {} {} {}'.format(iDev_plist['DeviceName'] , iDev_plist['ProductVersion'] , iDev_plist['DeviceColor'] , iDev_plist['HardwareModel']))
	checkVersion(iDev_plist['ProductVersion'])

def setup():
	if not os.path.exists('xml'):
		os.makedirs('xml')
	if not os.path.exists('txt'):
		os.makedirs('txt')

def checkVersion(iOSVer):
	#v7 = "7.0.6"
	v7 = "7.0.4"
	v71 = "7.1.1"
	v6 = "6.0.2"
	v61 = "6.1.6"
	v5 = "obsolete"

	if iOSVer == v7:
		print("You are runing: " + v7)

if __name__ == "__main__": main()
