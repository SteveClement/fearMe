fearMe
======

The F.E.A.R_me Project

This howto assumes:

HOME=/home/pi

REPO_DIR=/home/Desktop/code/fearMe

Dependencies to be installed on Raspbian:

```
 sudo apt-get install python-serial python3-serial python3-dev python3-rpi.gpio i2c-tools festival espeak xsel festlex-cmu arduino gcc-avr avr-libc avrdude libimobiledevice-utils vim tmux htop festvox-don festvox-rablpc16k festvox-kallpc16k festvox-kdlpc16k
```

Disable screen sleep
--------------------

If X is running:

```
sudo vi /etc/lightdm/lightdm.conf
xserver-command=X -s 0 dpms
```

If only on console:

```
sudo vi /etc/kbd/config
BLANK_TIME=0
POWERDOWN_TIME=0
```

raspian-config
--------------

Add:

```
LANG=en_GB.UTF-8
LC_ALL=en_GB.UTF-8
LANGUAGE=en_GB.UTF-8
```

To:
```
/etc/default/locale
```

python3-smbus
-------------

```
mkdir -p ~/Desktop/code/fearMe/Downloads
cd ~/Desktop/code/fearMe/Downloads
wget -c http://ftp.de.debian.org/debian/pool/main/i/i2c-tools/i2c-tools_3.1.0.orig.tar.bz2
tar xf i2c-tools_3.1.1.orig.tar.bz2
cd i2c-tools-3.1.1/py-smbus
cp smbusmodule.c smbusmodule.c.orig
cat ~/Desktop/code/fearMe/Patches/smbusmodule.c.diff | patch
wget -c http://github.com/groeck/lm-sensors/archive/V2-10-8.zip
unzip V2-10-8.zip
cp lm-sensors-2-10-8/kernel/include/i2c-dev.h .
rm -r lm-sensors-2-10-8*
python3 setup.py build
sudo python3 setup.py install
```

Arduino
-------

Fetch the submodules:

```
git submodule update --init
```

Copy the NeoPixel library:

```
mkdir -p ~/sketchbook/libraries
cp -r Adafruit_NeoPixel ~/sketchbook/libraries
```

Arduino upgrade
---------------

Upgrade to Arduino 1.6.2 (from 1.0.1) to use the Arduino micro board:

```
mkdir ~/Desktop/code/fearMe/Arduino/Downloads
cd ~/Desktop/code/fearMe/Arduino/Downloads
wget -c "http://arduino.cc/download.php?f=/arduino-1.6.2-linux32.tar.xz" -O arduino-1.6.2-linux32.xz
tar Jxvf arduino-1.6.2-linux32.xz
cd arduino-1.6.2
rm -rf hardware/tools
sudo cp -ru lib /usr/share/arduino
sudo cp -ru libraries /usr/share/arduino
sudo cp -ru tools /usr/share/arduino
sudo cp -ru hardware /usr/share/arduino
sudo cp -ru examples /usr/share/doc/arduino-core
sudo cp -ru reference /usr/share/doc/arduino-core
cd ..
rm -rf arduino-1.6.2
tar Jxvf arduino-1.6.2-linux32.xz
```

put this to your .bashrc

```
export ARDUINO_DIR=/home/pi/Desktop/code/fearMe/Arduino/Downloads/arduino-1.6.2
export ARDMK_DIR=/home/pi/Desktop/code/fearMe/Arduino-Makefile
export AVR_TOOLS_DIR=/usr
export EDITOR=vim
```

LCD Display
-----------

Add:

```
i2c-bcm2708
i2c-dev
```

To:

```
/etc/modules
```

Add your user to the group: i2c

```
sudo vigr
sudo vigr -s
```

High quality voices
-------------------

mbrola
------

These voices are provided by the MBROLA project, run by the TCTS Lab of the Faculté Polytechnique de Mons in Belgium. They offer several voices, in a variety of languages, which sound much better than the Festvox diphone voices. The database of voices can be viewed at the project's download page. See the voice demo page (the us1, us2 and us3 are the voices of interest). To use the MBROLA voices we need three parts: (1.) the mbrola binary program that parses a tokenstream the festival program feeds it and returns audio data back to festival, (2.) the MBROLA voices, and (3.) the Festvox wrappers to let the festival program use the voices. This may sound scary, but it's really very easy to do.

```
mkdir -p ~/Desktop/code/fearMe/Downloads
cd ~/Desktop/code/fearMe/Downloads
mkdir mbrola_tmp
cd mbrola_tmp/
wget -c http://tcts.fpms.ac.be/synthesis/mbrola/bin/raspberri_pi/mbrola.tgz
wget -c http://tcts.fpms.ac.be/synthesis/mbrola/dba/us1/us1-980512.zip
wget -c http://tcts.fpms.ac.be/synthesis/mbrola/dba/us2/us2-980812.zip
wget -c http://tcts.fpms.ac.be/synthesis/mbrola/dba/us3/us3-990208.zip
wget -c http://www.festvox.org/packed/festival/1.4.3/festvox_us1.tar.gz
wget -c http://www.festvox.org/packed/festival/1.4.3/festvox_us2.tar.gz
wget -c http://www.festvox.org/packed/festival/1.4.3/festvox_us3.tar.gz
unzip -x us1-980512.zip
unzip -x us2-980812.zip
unzip -x us3-990208.zip
tar zxvf festvox_us1.tar.gz
tar zxvf festvox_us2.tar.gz
tar zxvf festvox_us3.tar.gz
tar xfvz mbrola.tgz
sudo cp mbrola /usr/local/bin/
sudo mkdir -p /usr/share/festival/voices/english/us1_mbrola/
sudo mkdir -p /usr/share/festival/voices/english/us2_mbrola/
sudo mkdir -p /usr/share/festival/voices/english/us3_mbrola/
sudo mv us1 /usr/share/festival/voices/english/us1_mbrola/
sudo mv us2 /usr/share/festival/voices/english/us2_mbrola/
sudo mv us3 /usr/share/festival/voices/english/us3_mbrola/
sudo mv festival/lib/voices/english/us1_mbrola/* /usr/share/festival/voices/english/us1_mbrola/
sudo mv festival/lib/voices/english/us2_mbrola/* /usr/share/festival/voices/english/us2_mbrola/
sudo mv festival/lib/voices/english/us3_mbrola/* /usr/share/festival/voices/english/us3_mbrola/
cd ../
rm -rf mbrola_tmp/
```

CMU Arctic
----------
These voices were developed by the Language Technologies Institute at Carnegie Mellon University. They sound much better than both the diphone and the MBROLA voices. See the information page and voice demo page (the *_arctic_cg are the voices of interest). The drawback is that each voice takes over a hundred megs on disk, and with six English voices to choose from, that can take up a lot of bandwidth to download and depending on how much disk space you have to work with, six-hundred plus megs of space might be a bit much for voice data. However, the HTS voices discussed in the next section may in fact provide equal or better quality synthesis, and are only less than %2 of the size.

```
mkdir cmu_tmp
cd cmu_tmp/
wget -c http://www.speech.cs.cmu.edu/cmu_arctic/packed/cmu_us_awb_arctic-0.90-release.tar.bz2
wget -c http://www.speech.cs.cmu.edu/cmu_arctic/packed/cmu_us_bdl_arctic-0.95-release.tar.bz2
wget -c http://www.speech.cs.cmu.edu/cmu_arctic/packed/cmu_us_clb_arctic-0.95-release.tar.bz2
wget -c http://www.speech.cs.cmu.edu/cmu_arctic/packed/cmu_us_jmk_arctic-0.95-release.tar.bz2
wget -c http://www.speech.cs.cmu.edu/cmu_arctic/packed/cmu_us_ksp_arctic-0.95-release.tar.bz2
wget -c http://www.speech.cs.cmu.edu/cmu_arctic/packed/cmu_us_rms_arctic-0.95-release.tar.bz2
wget -c http://www.speech.cs.cmu.edu/cmu_arctic/packed/cmu_us_slt_arctic-0.95-release.tar.bz2
for t in `ls cmu_*` ; do tar xfj $t ; done
rm *.bz2
sudo mkdir -p /usr/share/festival/voices/english/
sudo mv * /usr/share/festival/voices/english/
for d in `ls /usr/share/festival/voices/english` ; do
if [[ "$d" =~ "cmu_us_" ]] ; then
	sudo mv "/usr/share/festival/voices/english/${d}" "/usr/share/festival/voices/english/${d}_clunits" 
fi ; done
cd ../
rm -rf cmu_tmp/
```

Nitech HTS
----------
These voices are produced by the HTS working group hosted at the Nagoya Institute of Technology. They have produced excellent quality voices which take up very little disk space. In terms of quality and size, probably the best (non-commercial) English voices availible for Festival. See the voice demo page (the *_arctic_hts are the voices of interest). Highly recommended. The voices are available on their download page.


```
mkdir hts_tmp
cd hts_tmp/
wget -c http://hts.sp.nitech.ac.jp/archives/2.1/festvox_nitech_us_awb_arctic_hts-2.1.tar.bz2
http://hts.sp.nitech.ac.jp/archives/2.2/
wget -c http://hts.sp.nitech.ac.jp/archives/2.1/festvox_nitech_us_bdl_arctic_hts-2.1.tar.bz2
wget -c http://hts.sp.nitech.ac.jp/archives/2.1/festvox_nitech_us_clb_arctic_hts-2.1.tar.bz2
wget -c http://hts.sp.nitech.ac.jp/archives/2.1/festvox_nitech_us_rms_arctic_hts-2.1.tar.bz2
wget -c http://hts.sp.nitech.ac.jp/archives/2.1/festvox_nitech_us_slt_arctic_hts-2.1.tar.bz2
wget -c http://hts.sp.nitech.ac.jp/archives/2.1/festvox_nitech_us_jmk_arctic_hts-2.1.tar.bz2
wget -c http://hts.sp.nitech.ac.jp/archives/1.1.1/cmu_us_kal_com_hts.tar.gz
wget -c http://hts.sp.nitech.ac.jp/archives/1.1.1/cstr_us_ked_timit_hts.tar.gz
for t in `ls` ; do tar xvf $t ; done
sudo mkdir -p /usr/share/festival/voices/us
sudo mv lib/voices/us/* /usr/share/festival/voices/us/
sudo mv lib/hts.scm /usr/share/festival/hts.scm
cd ../
rm -rf hts_tmp/
```

Testing
-------

```
for d in `ls /usr/share/festival/voices` ; do ls "/usr/share/festival/voices/${d}" ; done

$ festival
festival> (voice.list)
festival> (voice_us2_mbrola)
festival> (SayText "Hello from Ubuntu")
festival> (tts "story.txt" nil)
festival> (intro)
```

crontab
-------

Add:

```
@reboot ~/Desktop/code/fearMe/Scripts/fearMe_tmux.sh
5/* * * * * ~/Desktop/code/fearMe/Scripts/cleanUp.sh
```

to your $LUSER crontab

Finally, you can ask the plate which buttons are pressed with buttonPressed(lcd.BUTTONNAME) where BUTTONNAME is LEFT RIGHT UP DOWN or SELECT. This is not an interrupt-driven library so you can't have an interrupt go off when a button in pressed, instead you'll have to query the button in a loop. 
