#!/usr/bin/env python3

from subprocess import *

output=check_output("/home/pi/Desktop/code/fearMe/grabDev.sh", shell=True)

if output:
	print(output)
