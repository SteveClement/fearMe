#!/bin/bash

# Cleaning dmesg

# This is creep mode :)
#~/Desktop/code/fearMe/Scripts/grabDev.sh

# Running LCDtester
#~/Desktop/code/fearMe/LCDtest.py

# Running main script in safety loop:

~/Desktop/code/fearMe/Scripts/feedMe.sh &

while [ true ]; do
    ~/Desktop/code/fearMe/connDev.py
done
