from pytube import *
from time import sleep
import sys

def print_slow(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        sleep(0.1)

print("""\n\n\n

 _____     _           ______                    _                 _           
|_   _|   | |          |  _  \                  | |               | |          
  | |_   _| |__   ___  | | | |_____      ___ __ | | ___   __ _  __| | ___ _ __ 
  | | | | | '_ \ / _ \ | | | / _ \ \ /\ / / '_ \| |/ _ \ / _` |/ _` |/ _ \ '__|
  | | |_| | |_) |  __/ | |/ / (_) \ V  V /| | | | | (_) | (_| | (_| |  __/ |   
  \_/\__,_|_.__/ \___| |___/ \___/ \_/\_/ |_| |_|_|\___/ \__,_|\__,_|\___|_|   
                                                                               
                                                                               
\n\n""")

sleep(2)
Link = input("Enter The Youtube Video Link, Please\n")


try:
    video= YouTube(Link)
    print_slow("Link Is Valid\n\n")
except:
    print_slow("The link is not Correct please Double Check!")

sleep(2)
print_slow("\nStarting the Download ...\n")
stream= video.streams.get_highest_resolution()

try:
    stream.download()
    print_slow("\n\nDownload is Finished and Stored with your Script!")
except:
    print_slow("There is Error while Download the Video")
