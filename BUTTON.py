import os
from time import sleep

a ='\033[92m'
b ='\033[91m'
c ='\033[0m'
os.system('clear')
print (a+'\t          BUTTON TERMUX')
print (b+'\t               MR.Q')
print ('\t             Jokyworg')
print (a+'+'*55)
try:
     os.mkdir('/data/data/com.termux/files/home/.termux')
except:pass
key = "extra-keys = [['ESC','/','-','HOME','UP','END','PGUP'],['TAP','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN']]"
fan = open('/data/data/com.termux/files/home/.termux/termux.properties','w')
fan.write(key)
fan.close ()
os.system ('termux-reload-settings')
print (a+'[!] SUKSES MENAMBAHKAN TOMBOL... '+c+'\n\nSUBSCRIBE YOUTUBE : JOKYWORG\n\n')


