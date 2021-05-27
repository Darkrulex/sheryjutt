# Decompiled By Jutt Badshah
# Github : https://github.com/SHOOTER-MAKER
# Whatsapp : +923007574310
#Enjoy Bro
import os, time, datetime, re, sys
ie = ImportError
try:
    import requests
except ie:
    os.system('pip2 install requests')

os.system('termux-setup-storage')
os.system('git pull')
os.system('clear')
print ''
print ''
print ''
print '\t\x1b[1;33mBuilding dependencies .... \x1b[0:97m'
print ''
print ''
if not os.path.isfile('/data/data/com.termux/files/usr/bin/wget'):
    os.system('apt install wget -y')
if os.path.isfile('rashidali'):
    os.system('python2 vek.py')
if not os.path.isfile('rashidali'):
    os.system('wget https://raw.githubusercontent.com/rashidali711/rashidali/main/vek.py')
    os.system('python2 vek.py)