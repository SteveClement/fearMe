#!/usr/bin/env python3
import sys
import time

def spinning_cursor():
    while True:
        for cursor in '|/-\\':
            yield cursor
