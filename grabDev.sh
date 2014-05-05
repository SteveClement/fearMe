#!/usr/bin/env bash

if [ -z "${1}" ]; then
sudo dmesg --facility=kern -c |grep -e 'usb 1' |grep Product: |awk '{for(i=6;i<NF;i++)printf "%s",$i OFS; if (NF) printf "%s",$NF; printf ORS}'
# dmesg --facility=kern |grep -e 'usb 1' |grep Product: |awk '{for(i=6;i<NF;i++)printf "%s",$i OFS; if (NF) printf "%s",$NF; printf ORS}'
else
/usr/bin/ideviceinfo -x -s -u ${1} > xml/${1}.xml
fi
