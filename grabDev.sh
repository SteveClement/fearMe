#!/usr/bin/env bash

usb_product=`dmesg --facility=kern |grep -e 'usb 1' |grep Product: |awk '{for(i=6;i<NF;i++)printf "%s",$i OFS; if (NF) printf "%s",$NF; printf ORS}'`

if [ -n "${usb_product}" ]; then
	echo -n "Product:"
	dmesg --facility=kern |grep -e 'usb 1' |grep Product: |awk '{for(i=6;i<NF;i++)printf "%s",$i OFS; if (NF) printf "%s",$NF; printf ORS}'
	echo -n "Manufacturer:"
	dmesg --facility=kern |grep -e 'usb 1' |grep Manufacturer: |awk '{for(i=6;i<NF;i++)printf "%s",$i OFS; if (NF) printf "%s",$NF; printf ORS}'
	sudo dmesg --facility=kern -c |grep -e 'usb 1' |grep idVendor |awk '{for(i=8;i<NF;i++)printf "%s",$i OFS; if (NF) printf "%s",$NF; printf ORS}'
fi


if [ -n "${1}" ]; then
	/usr/bin/ideviceinfo -x -s -u ${1} > xml/${1}.xml
fi
