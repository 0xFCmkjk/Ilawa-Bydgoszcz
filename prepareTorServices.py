import os

def installServices():
    os.system("cd Tor")
    os.system("tor.exe --service install")

def startServices():
    os.system("cd Tor")
    os.system("tor.exe --service start")

def stopServices():
    os.system("cd Tor")
    os.system("tor.exe --service stop") #some