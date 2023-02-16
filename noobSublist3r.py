from colorama import Fore
import threading
import requests
import sys
import subprocess

print(Fore.MAGENTA+"""
                   _     ______       _     _  _            ______        
                  | |   / _____)     | |   | |(_)       _  (_____ \       
 ____   ___   ___ | |__( (____  _   _| |__ | | _  ___ _| |_ _____) ) ____ 
|  _ \ / _ \ / _ \|  _ \\____ \| | | |  _ \| || |/___|_   _|_____ ( / ___)
| | | | |_| | |_| | |_) )____) ) |_| | |_) ) || |___ | | |_ _____) ) |    
|_| |_|\___/ \___/|____(______/|____/|____/ \_)_(___/   \__|______/|_|    
                                                                          
AUTHOR : Ghost
GitHub : mdk4if

""")

usage = Fore.RED+"python3 noobSublist3r.py <domain name> <output file name/path>"
if len(sys.argv) != 3:
    print(usage)
    quit()
domain = sys.argv[1]
output = open(sys.argv[2],"a")
subdomainFile = open("subdomains.txt","r")
def findsub():
    for count,subdomainName in enumerate(subdomainFile):
        subdomainName = subdomainName.strip("\n")
        url = f"https://{subdomainName}.{domain}"
        try:
            if requests.get(url,timeout=4):
                print(Fore.GREEN+"[+]"+str(url))
                output.write(str(url) + "\n")
                requests.close()
        except:
            pass

threads = []
for i in range(20):
    t = threading.Thread(target=findsub)
    t.daemon = True
    threads.append(t)
for i in range(20):
    threads[i].start()

for i in range(20):
    threads[i].join()
