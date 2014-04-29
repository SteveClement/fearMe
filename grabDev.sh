#!/usr/bin/env sh

sudo dmesg --facility=kern -c |grep -e 'usb 1' |grep Product: |awk '{for(i=6;i<NF;i++)printf "%s",$i OFS; if (NF) printf "%s",$NF; printf ORS}'
# dmesg --facility=kern |grep -e 'usb 1' |grep Product: |awk '{for(i=6;i<NF;i++)printf "%s",$i OFS; if (NF) printf "%s",$NF; printf ORS}'
