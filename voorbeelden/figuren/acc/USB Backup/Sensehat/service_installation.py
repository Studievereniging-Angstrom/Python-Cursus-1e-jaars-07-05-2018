import os

"""
Run this script to install and activate sensehat.service
Tested on a: Raspbian GNU/Linux 9 (stretch)

Sensehat.py should start up if the installation is succesful. 
"""

os.system('sudo cp /media/pi/DATA/Sensehat/sensehat.service /lib/systemd/system/sensehat.service')
os.system('sudo chmod 644 /lib/systemd/system/sensehat.service')
os.system('chmod +x /media/pi/DATA/Sensehat/sensehat.py')
os.system('sudo systemctl daemon-reload')
os.system('sudo systemctl enable sensehat.service')
os.system('sudo systemctl start sensehat.service')
print('Installation finished.')