﻿from colorama import Fore, Back, Style
import os
import pyttsx3
import sys
import platform
import requests
import time
key = ("linhdzhaha")
nhap_key = input(Fore.CYAN +"vui lòng nhập key: ")
if key == nhap_key:
	print (Fore.RED +"đúng key vào tool ngay")
else:
    print (Fore.RED +"sai key vui lòng thử lại")
    quit()
        
    
    #Chuẩn bị
print(Fore.BLUE +"\nĐang vào sever ddos của PHẠM BẢO LINH!")
for i in range(5,0,-1):
    print(i,end=" ",flush=True)
    time.sleep(1)
print(Fore.YELLOW +"\nok")
from colorama import Fore, Back, Style
import os
import pyttsx3
import sys
import platform
def say_stuff(stuff_to_say):
    engine = pyttsx3.init()
    engine.say(str(stuff_to_say))
    engine.runAndWait()
if str(platform.system()) == 'Linux':
    os.system('')
print (Fore.BLUE +"---------------------------------------------------------------------")
print (Fore.CYAN +"| CRE : LINHPHAM|TOOL KATANA V1                                     |")
print (Fore.CYAN +"| FACEBOOK : https://www.facebook.com/tgtgn                         |")
print (Fore.CYAN +"|                                                                   |")
print (Fore.BLUE +"---------------------------------------------------------------------")
try:
    site = input(Fore.LIGHTGREEN_EX+"╔═══"+Fore.CYAN+"["+Fore.LIGHTGREEN_EX+"Url"+Fore.CYAN+"]"+Fore.LIGHTGREEN_EX+"\n╚══\x1b[38;2;0;255;189m> "+Fore.WHITE)
    threads = input('  \x1b[38;2;255;20;147m•' + Fore.WHITE + 'Time(s): ')
    print('')
    text = print(Fore.GREEN + 'ĐANG KHỞI ĐỘNG TOOL . . .')

    if 'Windows' in str(platform.system()):
        os.system('go run tool.go -site {0}'.format(site))
    else:
        os.system('NQHTOOL={0} go run tool.go -site {1}'.format(threads,site))
    print(Back.BLACK + Fore.GREEN)
    
except:
    print('[+] Installing Dependancies')
    os.system('python3 Install_Dependancies.py')
    os.system('python Install_Dependancies.py')
    os.system('py Install_Dependancies.py')