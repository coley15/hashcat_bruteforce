import os
import subprocess
from termcolor import colored
from time import sleep
import shutil

intro_art = """ __      __.__  _____.__  ___.                 __          _____                           
/  \    /  \__|/ ____\__| \_ |_________ __ ___/  |_  _____/ ____\___________   ____  ____  
\   \/\/   /  \   __\|  |  | __ \_  __ \  |  \   __\/ __ \   __\/  _ \_  __ \_/ ___\/ __ \ 
 \        /|  ||  |  |  |  | \_\ \  | \/  |  /|  | \  ___/|  | (  <_> )  | \/\  \__\  ___/ 
  \__/\  / |__||__|  |__|  |___  /__|  |____/ |__|  \___  >__|  \____/|__|    \___  >___  >
       \/                      \/                       \/                        \/    \/ 
                                                                                           
                                                                                           
___.                        .__                 ____ .________                             
\_ |__ ___.__.   ____  ____ |  |   ____ ___.__./_   ||   ____/                             
 | __ <   |  | _/ ___\/  _ \|  | _/ __ <   |  | |   ||____  \                              
 | \_\ \___  | \  \__(  <_> )  |_\  ___/\___  | |   |/       \                             
 |___  / ____|  \___  >____/|____/\___  > ____| |___/______  /                             
     \/\/           \/                \/\/                 \/                              \n"""


def draw_intro():
    print(colored(intro_art, 'red'))
    print("REQUIREMENTS:")
    print("     [1]. WIFI CRACKING IS ONLY COMPATIABLE WITH HC22000 FILES ")
    print("     [2]. HASHCAT MUST BE ADDED TO PATH ")


def check_install():

    print("\nChecking for installation...\n")
    sleep(0.1)

    hashcat_path = input("Please enter the path to your hashcat file: ")

    try: 
        os.chdir(hashcat_path)

    except Exception as e: 
        print(F"Please enter a valid path to your hashcat directory: {e}")

def run_hashcat(hashfile, wordlist):
    
    command = ['hashcat', '-m', '22000', '-a', '0', hashfile, wordlist, '--status', '--status-timer', '10', '-w', '3']

    try:
        # Run the command using subprocess
        subprocess.Popen(['start', 'cmd', '/K'] + command, shell=True)

    except subprocess.CalledProcessError as e:
        print("Error occurred while running hashcat:", e.stderr)


def main():
    
    draw_intro()
    check_install()

    hashfile = input("Please enter the path to your hc22000 file: ")
    wordlist = input("Please enter the path to your word list: ")

    run_hashcat(hashfile, wordlist)


main()