#!/usr/bin/env bash

touch ~/Desktop/code/fearMe/txt/pre_usb.txt

usb_product=`dmesg --facility=kern |grep -P "usb usb[1-99]:|usb [1-9]-[1-9]:" |grep Product: |cut -f 2- -d:|cut -f 2- -d:`

# Really make sure if something happens on the usb bus  we actually catch it
current_connections=`lsusb |wc -l`
# Careful if txt/pre_usb.txt is NULL the if fails
previous_connections=`cat txt/pre_usb.txt`

#if [ "${current_connections}" -lt "${previous_connections}" ]; then
if ((${current_connections} != ${previous_connections})); then
	echo -n "Product:"
	dmesg --facility=kern |grep -P "usb usb[1-99]:|usb [1-9]-[1-9]:" |grep Product: |cut -f 2- -d:|cut -f 2- -d:
	echo -n "Manufacturer:"
	dmesg --facility=kern |grep -P "usb usb[1-99]:|usb [1-9]-[1-9]:" |grep Manufacturer: |cut -f 2- -d:|cut -f 2- -d:
	echo ${current_connections} > txt/pre_usb.txt
	usb_product=1
fi

if [ -n "${usb_product}" ]; then
	echo -n "Product:"
	dmesg --facility=kern |grep -P "usb usb[1-99]:|usb [1-9]-[1-9]:" |grep Product: |cut -f 2- -d:|cut -f 2- -d:
	echo -n "Manufacturer:"
	dmesg --facility=kern |grep -P "usb usb[1-99]:|usb [1-9]-[1-9]:" |grep Manufacturer: |cut -f 2- -d:|cut -f 2- -d:
	sudo dmesg --facility=kern -c |grep -P "usb usb[1-99]:|usb [1-9]-[1-9]:" |grep idVendor |cut -f2 -d, |cut -f2 -d=
fi

if [ -n "${1}" ]; then
	/usr/bin/ideviceinfo -x -s -u ${1} > xml/${1}.xml
fi
