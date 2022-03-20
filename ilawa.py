import time
print(""" 
$$$$$$\ $$\                                           $$$$$$$\                  $$\                                                             
\_$$  _|$$ |                                          $$  __$$\                 $$ |                                                            
  $$ |  $$ | $$$$$$\  $$\  $$\  $$\  $$$$$$\          $$ |  $$ |$$\   $$\  $$$$$$$ | $$$$$$\   $$$$$$\   $$$$$$$\ $$$$$$$$\  $$$$$$$\ $$$$$$$$\ 
  $$ |  $$ | \____$$\ $$ | $$ | $$ | \____$$\ $$$$$$\ $$$$$$$\ |$$ |  $$ |$$  __$$ |$$  __$$\ $$  __$$\ $$  _____|\____$$  |$$  _____|\____$$  |
  $$ |  $$ | $$$$$$$ |$$ | $$ | $$ | $$$$$$$ |\______|$$  __$$\ $$ |  $$ |$$ /  $$ |$$ /  $$ |$$ /  $$ |\$$$$$$\    $$$$ _/ $$ /        $$$$ _/ 
  $$ |  $$ |$$  __$$ |$$ | $$ | $$ |$$  __$$ |        $$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ |$$ |  $$ | \____$$\  $$  _/   $$ |       $$  _/   
$$$$$$\ $$ |\$$$$$$$ |\$$$$$\$$$$  |\$$$$$$$ |        $$$$$$$  |\$$$$$$$ |\$$$$$$$ |\$$$$$$$ |\$$$$$$  |$$$$$$$  |$$$$$$$$\ \$$$$$$$\ $$$$$$$$\ 
\______|\__| \_______| \_____\____/  \_______|        \_______/  \____$$ | \_______| \____$$ | \______/ \_______/ \________| \_______|\________|
                                                                $$\   $$ |          $$\   $$ |                                                  
                                                                \$$$$$$  |          \$$$$$$  |                                                  
                                                                 \______/            \______/   version: Dev i guess
\n""")
time.sleep(0.69)
print("Ilawa >> Welcome to DOS tool, this shit is created only for educational purposes, don't use this to do bad things like turning off your mom's pornhub page! \n")
time.sleep(0.69)
print("Ilawa >> This lovely tool works only on Windows, if u're using this, probably u're not smart enough to use linux. \n")
time.sleep(0.69)
print("Ilawa >> We need to verify that u're not drunk, and u know what u're doing. Rewrite this phrase: '\033[1m IMSUCHADUMBGUYMYMOMDOPORNHUB \033[0m'\n")
time.sleep(0.69)
phs = input()

if phs == "IMSUCHADUMBGUYMYMOMDOPORNHUB": #if clausule 
    
    userAgent = "ukraini slava"
    cooldown = 1

    print("Ilawa >> Verication passed. \n")
    print("Ilawa >> WARNING! TO EXIT PROGRAM PRESS CTRL+C \n")
    print("Ilawa >> Now this tool works only in UDP mode!")
    import attack #if u do not understand this u're dumbo
    import prepareTorServices #imports prepareTorServices.py, this module enables tor-service for attack niggere

    import os
    #print("Ilawa >> Downloading TOR Expert bundle, it will be used to hide u from ur mom and police... \n")
    #if os.path.exists("Tor.zip") is False:
    #    os.system("wget https://cdn-132.anonfiles.com/n4u9veK0x0/98d58f6f-1645867289/Tor.zip") #TOR windows expert bundle on anonfiles
    #    print("Ilawa >> Download probably done \n")
    #    print("Ilawa >> Unziping... \n")
    #    os.system("unzip Tor.zip \n") #unzips Tor.zip (downloaded file)
    #    print("Ilawa >> Unzip probably done! \n")
    #elif os.path.exists("Tor"):
    #    print("Ilawa >> Tor folder exists, skipping download procces...")

    #print("Ilawa >> Installing TorServices...")
    #prepareTorServices.installServices()

    #print("Ilawa >> Starting TorServices...")
    #prepareTorServices.startServices() ahahahahahahhahahhahah

    print("Ilawa >> Now u have to put in some data! \n")
    ip = input("Put ur target ip/url \n")
    port = input("Put port that will be attacked \n")
    nawalki = input("Put number of threadads that will make attack (bigger number = better results) max 100 \n")
    cooldown = input("Put cooldown time in miliseconds (cooldown before sending next package) deafult: 1 \n")
        
    if ip is not None and port is not None and nawalki is not None and cooldown is not None:
        print("Ilawa >> All the data has been put \n")
        print("Are u sure that u want make DoS attack ONLY for educational purposes? [Y/n]")
        confirm = input()
        if confirm == "Y" or "y":
            attack.enableAttack(ip=ip, port=port, threadsCount=int(nawalki), cooldown=int(cooldown))
            print(r"Ilawa >> Я НАЧИНАЮ АТАКУ")
            print(r"ПОДГОТОВЬТЕСЬ К ИНТЕРЕСНЫМ ЭФФЕКТАМ")
            print(r"МЫ УДАРЯЕМ")

        
        else:
            print("Quiting the program, NAURA!")
            quit()

    else:
        print("Ilawa >> Data Error")
        
else:
    print("Ilawa >> Veryfication Passn't lmao")