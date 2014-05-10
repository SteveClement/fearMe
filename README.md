fearMe
======

The F.E.A.R_me Project

Dependencies for the code included here:


 sudo apt-get install python-serial python-smbus i2c-tools festival pyttsx espeak xsel festlex-cmu


Add:

i2c-bcm2708
i2c-dev

To:
/etc/modules

High quality voices:

cd /usr/share/festival/voices/english/
sudo wget -c http://www.speech.cs.cmu.edu/cmu_arctic/packed/cmu_us_clb_arctic-0.95-release.tar.bz2
sudo tar jxf cmu_us_clb_arctic-0.95-release.tar.bz2 
sudo ln -s cmu_us_clb_arctic cmu_us_clb_arctic_clunits
sudo cp /etc/festival.scm /etc/festival.scm.backup
sudo echo "(set! voice_default 'voice_cmu_us_clb_arctic_clunits)" >> /etc/festival.scm

