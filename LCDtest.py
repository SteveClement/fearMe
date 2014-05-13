#!/usr/bin/env python3

from time import sleep
from Adafruit_CharLCDPlate import Adafruit_CharLCDPlate

# Initialize the LCD plate.  Should auto-detect correct I2C bus.  If not,
# pass '0' for early 256 MB Model B boards or '1' for all later versions
lcd = Adafruit_CharLCDPlate()

#lcd.begin(16, 4)
lcd.begin(16, 2)

# Clear display and show greeting, pause 1 sec
lcd.clear()
lcd.backlight(lcd.GREEN)
lcd.blink()

msg = "Welcome to uni  charge"

for a in range(0,len(msg)):
    if a == 16:
        lcd.message("\n")
    lcd.message(msg[a],0)
    sleep(.2)
    #lcd.scrollDisplayLeft()
#sleep(1)

# Cycle through backlight colors
col = (lcd.RED , lcd.YELLOW, lcd.GREEN, lcd.TEAL,
       lcd.BLUE, lcd.VIOLET, lcd.ON   , lcd.OFF)
for c in col:
    lcd.backlight(c)
    sleep(.3)

# Poll buttons, display message & set backlight accordingly
# 16x2 wrap:
#btn = ((lcd.LEFT  , 'This is a very l\ong line to see where th\is code will wrape the line :)'              , lcd.RED),
# 16x4 wrap:
#btn = ((lcd.LEFT  , 'This is a very long \line to see where th\is code will wrape t\he line :)'              , lcd.RED),
btn = ((lcd.LEFT  , 'This is a very long line to see where this code will wrape the line :)'              , lcd.RED),
       (lcd.UP    , 'Sita sings\nthe blues'     , lcd.BLUE),
       (lcd.DOWN  , 'I see fields\nof green'    , lcd.GREEN),
       (lcd.RIGHT , 'Purple mountain\nmajesties', lcd.VIOLET),
       (lcd.SELECT, 'GoodBye'                          , lcd.VIOLET))
prev = -1
lcd.clear()
lcd.message("Now ready!\nPlug in your test device",1)
while True:
    for b in btn:
        if lcd.buttonPressed(b[0]):
            if b is not prev:
                if b[0] == 0:
                    break
                lcd.clear()
                lcd.message(b[1],1)
                lcd.backlight(b[2])
                prev = b
            break
