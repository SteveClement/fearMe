fearMe
======

The F.E.A.R_me Project

This howto assumes:

HOME=/home/pi
REPO_DIR=/home/Desktop/code/fearMe

Dependencies to be installed on Raspbian:

 sudo apt-get install python-serial python-smbus i2c-tools festival pyttsx espeak xsel festlex-cmu arduino gcc-avr avr-libc avrdude



Arduino
-------

Fetch the NeoPixel library:

cd ~/sketchbook/libraries
git clone git@github.com:SteveClement/Adafruit_NeoPixel.git

Get the Arduino-Makfile project:

cd ~/Desktop/code
git clone https://github.com/sudar/Arduino-Makefile.git

Upgrade to Arduino 1.0.5 to use the Arduino micro board:

mkdir ~/Desktop/code/fearMe/Arduino/Downloads
cd ~/Desktop/code/fearMe/Arduino/Downloads
wget http://arduino.googlecode.com/files/arduino-1.0.5-linux32.tgz
tar zxvf arduino-1.0.5-linux32.tgz
cd arduino-1.0.5
rm -rf hardware/tools
sudo cp -ru lib /usr/share/arduino
sudo cp -ru libraries /usr/share/arduino
sudo cp -ru tools /usr/share/arduino
sudo cp -ru hardware /usr/share/arduino
sudo cp -ru examples /usr/share/doc/arduino-core
sudo cp -ru reference /usr/share/doc/arduino-core
cd ..
rm -rf arduino-1.0.5
tar zxvf arduino-1.0.5-linux32.tgz

put this to your .bashrc

export ARDUINO_DIR=/home/pi/Desktop/code/fearMe/Arduino/Downloads/arduino-1.0.5
export ARDMK_DIR=/home/pi/Desktop/code/Arduino-Makefile
export AVR_TOOLS_DIR=/usr

LCD Display
-----------

Add:

i2c-bcm2708
i2c-dev

To:
/etc/modules

High quality voices
-------------------

cd /usr/share/festival/voices/english/
sudo wget -c http://www.speech.cs.cmu.edu/cmu_arctic/packed/cmu_us_clb_arctic-0.95-release.tar.bz2
sudo tar jxf cmu_us_clb_arctic-0.95-release.tar.bz2 
sudo ln -s cmu_us_clb_arctic cmu_us_clb_arctic_clunits
sudo cp /etc/festival.scm /etc/festival.scm.backup
sudo echo "(set! voice_default 'voice_cmu_us_clb_arctic_clunits)" >> /etc/festival.scm

