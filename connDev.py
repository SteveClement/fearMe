#!/usr/bin/env python3

from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate

from subprocess import *
from plistlib import *
from time import *
from os.path import expanduser
from datetime import datetime
import os
from datetime import datetime
import spinner

spinner = spinner.spinning_cursor()

lcd = Adafruit_CharLCDPlate()
lcd.begin(16,2)
lcd.backlight(lcd.GREEN)
lcd.blink()

cmd = "ip addr show eth0 | grep inet | awk '{print $2}' | cut -d/ -f1"
safetyMessage="Your device is very safe now."
welcomeMessage="Starting up"
goodHandsMessage="Your data is\nin good hands."
inciteMessage="Please connect your device"

runOnce = True

debug = {'glob': False, 'lcd': False }
feature = {'lcd': True, 'audio': True, 'arduino': True, 'creep': True}

lcd_debug = False
startTime=lastOutput=lastTimeout=int(time())

def run_cmd(cmd):
        p = Popen(cmd, shell=True, stdout=PIPE)
        output = p.communicate()[0]
        return output

def sayStuff(msg):
	festival = "/usr/bin/festival"
	festival_opts = "--tts"
	festival_file = "/tmp/say.txt"
	fh = open(festival_file, "w")
	print(msg, file=fh)
	fh.close()

	print("Saying: " + msg)
	check_output([festival, festival_opts, festival_file])

def main():
	global lastOutput
	global startTime
	global lastTimeout

	iDevDupeCount = 0

	ipaddr = setup()
	if debug['lcd']:
		lcd.message('IP %s' % ( str(ipaddr) ) )
	lcd.clear()
	lcd.message('Please connect\nyour device...')
	home = expanduser("~")
	code = "/Desktop/code/fearMe"
	grabDev = home + code + "/Scripts/grabDev.sh"

	fhCH = open('txt/connectionHistory.txt','a')

	output=check_output(grabDev, shell=True)
	if ((lastOutput - startTime) > 30) or ((int(time() - lastTimeout) > 180)):
		print("#timeout")
		timeout()
		lastTimeout=int(time())
	print(output)

	try:
		attached_iDevices = str(check_output(["/usr/bin/idevice_id", "-l"])).rstrip().split('\\n')
		iDev = True
		if debug['lcd']:
			lcd.clear()
			lcd.message("Grabbing attached iDevices")
	except:
		iDev = False
		if debug['lcd']:
			lcd.clear()
			lcd.message("No iDevice connected, move along")

	if output:
		lastOutput=int(time())
		print(output, file=fhCH)
		attachedDevices=str(output).rstrip().split('\\n')
		print(attachedDevices[0][2:].split(":")[0] + ":" + attachedDevices[0][2:].split(":")[1])
		attachedDevice = attachedDevices[0][2:].split(":")[1].replace("iPhone", "eye Phone")
		attachedDevice = attachedDevices[0][2:].split(":")[1].replace("iPad", "eye Pad")
		print(attachedDevice)
		lcd.backlight(lcd.RED)
		msg = "Hello:\n " + attachedDevice
		lcd.clear()
		lcd.message(msg)
		msg2 = "Hello " + attachedDevice
		sayStuff(msg2)
		#sayStuff(goodHandsMessage)
		print(attachedDevices[1].split(":")[0] + ":" + attachedDevices[1].split(":")[1])
		fhCH.close()

	if iDev:
		if ( len(attached_iDevices) > 2 ):
			print("More than 1 iDevice detected")
			iDev_1 = attached_iDevices[0][2:]
			iDev_2 = attached_iDevices[1]

			if ( os.path.isfile('xml/' + iDev_1 + '.xml') ):
				print("We have this device already")
				if iDevDupeCount < 3:
					iDevDupeCount += 1
					iDevDupe = True
				else:
					iDevDupe = False
				readDev(iDev_1, iDevDupe)
			else:
				iDev1XML = Popen([grabDev, iDev_1], shell=False)
				iDevDupe = False
				readDev(iDev_1, iDevDupe)

			if ( os.path.isfile('xml/' + iDev_2 + '.xml') ):
				print("We have this device already")
				if iDevDupeCount < 3:
					iDevDupeCount += 1
					iDevDupe = True
				else:
					iDevDupe = False
				readDev(iDev_2, iDevDupe)
			else:
				iDev2XML = Popen([grabDev, iDev_2], shell=False)
				iDevDupe = False
				readDev(iDev_2, iDevDupe)

		else:
			iDev = attached_iDevices[0][2:]

			if ( os.path.isfile('xml/' + iDev + '.xml') ):
				print("We have this device already")
				iDevDupe = True
				readDev(iDev, iDevDupe)
			else:
				iDevXML = Popen([grabDev, iDev], shell=False)
				iDevDupe = False
				readDev(iDev, iDevDupe)
#	else:
#		sayStuff(safetyMessage)

def readDev(iDev, iDevDupe=False):
	# Sleep to allow write to disk! (which is weird because the shell script is done and no file on disk)
	while True:
		try:
			iDev_plist = readPlist('xml/' + iDev + '.xml')
			break
		except:
			continue

	if (iDev_plist['DeviceColor'] == '#3b3b3c' or iDev_plist['DeviceColor'] == '#e1e4e3'):
		iDev_plist['DeviceColor'] = 'grey'
	iDevName = iDev_plist['DeviceName'].replace("'", "")
	iDevName = iDev_plist['DeviceName'].replace("’", "")
	iDevName = iDevName.replace("iPhone", "eye Phone")
	iDevName = iDevName.replace("iPad", "eye Pad")
	print(iDevName)
	iDevVersion = iDev_plist['ProductVersion']
	iDevColor = iDev_plist['DeviceColor']

	try:
		iDevPad = iDevName.index("iPad")
	except:
		iDevPad = False

	##print('Device specs: {} {} {} {}'.format(iDev_plist['DeviceName'] , iDev_plist['ProductVersion'] , iDev_plist['DeviceColor'] , iDev_plist['HardwareModel']))
	#UnicodeEncodeError: 'ascii' codec can't encode character '\u2019' in position 27: ordinal not in range(128)
	if not iDevDupe:
		if iDevPad:
			#sayStuff("You own an eye Device, you are probably from Luxembourg, taking extra good care of your data.")
			sayStuff("Hello " + iDevName + ". Your device is running version " + iDevVersion + " and the color you choose " + iDevColor)
		else:
			sayStuff("Hello " + iDevName + ". Your device is running version " + iDevVersion + " and the color you choose " + iDevColor)

		sayStuff(safetyMessage)
	checkVersion(iDev_plist['ProductVersion'])

def setup():
	global runOnce
	ipaddr = run_cmd(cmd)
	if runOnce:
		#sayStuff("Welcome to the Universal charging station.")
		lcd.message(welcomeMessage)
		sleep(1)
		lcd.clear()
		for _ in range(10):
			lcd.message(next(spinner))
			sleep(.3)
			lcd.clear()
		if not os.path.exists('xml'):
			os.makedirs('xml')
		if not os.path.exists('txt'):
			os.makedirs('txt')
		runOnce=False
	return ipaddr

def timeout():
	lcd.clear()
	lcd.message("Timeout reached")
	for _ in range(0,2):
		lcd.backlight(lcd.RED)
		sleep(.5)
		lcd.backlight(lcd.WHITE)
		sleep(.5)
		lcd.backlight(lcd.BLUE)
		sleep(.5)

def checkVersion(iOSVer):
	#v7 = "7.0.6"
	v7 = "7.0.4"
	v71 = "7.1.1"
	v6 = "6.0.2"
	v61 = "6.1.6"
	v5 = "obsolete"

	if iOSVer == v7:
		print("You are runing: " + v7)

if __name__ == "__main__":
	while True:
		main()
		print("Sleeping")
		sleep(.5)
		lcd.clear()
		lcd.backlight(lcd.GREEN)
		#lcd.message(datetime.now().strftime('%b %d\n  %H:%M:%S\n'))
