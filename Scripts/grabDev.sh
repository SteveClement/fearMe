#!/usr/bin/env bash

touch ~/Desktop/code/fearMe/txt/pre_usb.txt

usb_product=`dmesg --facility=kern |grep -e 'usb 1' |grep Product: |awk '{for(i=6;i<NF;i++)printf "%s",$i OFS; if (NF) printf "%s",$NF; printf ORS}'`

# Really make sure if something happens on the usb bus  we actually catch it
current_connections=`lsusb |wc -l`
previous_connections=`cat txt/pre_usb.txt`

#if [ "${current_connections}" -lt "${previous_connections}" ]; then
if ((${current_connections} != ${previous_connections})); then
	echo -n "Product:"
        #dmesg --facility=kern |grep -e 'usb' |grep Product: |awk '{for(i=6;i<NF;i++)printf "%s",$i OFS; if (NF) printf "%s",$NF; printf ORS}'
        dmesg --facility=kern |grep -e 'usb' |grep Product: |awk '{for(i=5;i<NF;i++)printf "%s",$i OFS; if (NF) printf "%s",$NF; printf ORS}'
	echo -n "Manufacturer:"
	#dmesg --facility=kern |grep -e 'usb' |grep Manufacturer: |awk '{for(i=6;i<NF;i++)printf "%s",$i OFS; if (NF) printf "%s",$NF; printf ORS}'
	dmesg --facility=kern |grep -e 'usb' |grep Manufacturer: |awk '{for(i=5;i<NF;i++)printf "%s",$i OFS; if (NF) printf "%s",$NF; printf ORS}'
	echo ${current_connections} > txt/pre_usb.txt
	usb_product=1
fi

if [ -n "${usb_product}" ]; then
	echo -n "Product:"
	#dmesg --facility=kern |grep -e 'usb 1' |grep Product: |awk '{for(i=6;i<NF;i++)printf "%s",$i OFS; if (NF) printf "%s",$NF; printf ORS}'
	dmesg --facility=kern |grep -e 'usb 1' |grep Product: |awk '{for(i=5;i<NF;i++)printf "%s",$i OFS; if (NF) printf "%s",$NF; printf ORS}'
	echo -n "Manufacturer:"
	#dmesg --facility=kern |grep -e 'usb 1' |grep Manufacturer: |awk '{for(i=6;i<NF;i++)printf "%s",$i OFS; if (NF) printf "%s",$NF; printf ORS}'
	dmesg --facility=kern |grep -e 'usb 1' |grep Manufacturer: |awk '{for(i=5;i<NF;i++)printf "%s",$i OFS; if (NF) printf "%s",$NF; printf ORS}'
	#sudo dmesg --facility=kern -c |grep -e 'usb 1' |grep idVendor |awk '{for(i=8;i<NF;i++)printf "%s",$i OFS; if (NF) printf "%s",$NF; printf ORS}'
	sudo dmesg --facility=kern -c |grep -e 'usb 1' |grep idVendor |awk '{for(i=7;i<NF;i++)printf "%s",$i OFS; if (NF) printf "%s",$NF; printf ORS}'
fi

if [ -n "${1}" ]; then
	/usr/bin/ideviceinfo -x -s -u ${1} > xml/${1}.xml
fi
