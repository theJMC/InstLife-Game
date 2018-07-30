
import time
import os

def install():
    print("Installing the required packages...")
    try:
        print("Installing...")
        try:
            os.system('pip install appjar')
        except: 
            print("A Problem has occured installing appJar, a required dependency for the game to work")
        try:
        os.system('git clone https://github.com/QPJAY/InstLife-Game.git')
        except: 
            print("A Problem Has Occured downloading the game files, please check if you have internet connection")
    except:
        print("A general problem has occured, please file an issue on github.")

install()