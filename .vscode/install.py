from pip._internal import main as pipmain
import time
import os

def install():
    print("Installing the required packages...")
    try:
        print("Installing...")
        # pipmain(['install', 'appJar'])
        os.system('git clone https://github.com/QPJAY/InstLife-Game.git')
    except:
        print("Something has not worked in the installation phase. Either the required package is already installed, or pip broke!")

install()