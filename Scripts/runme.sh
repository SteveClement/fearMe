#!/bin/bash

# Cleaning dmesg

~/Desktop/code/fearMe/Scripts/grabDev.sh

# Running LCDtester
#~/Desktop/code/fearMe/LCDtest.py

# Running main script in safety loop:

while [ true ]; do
    ~/Desktop/code/fearMe/connDev.py
done
