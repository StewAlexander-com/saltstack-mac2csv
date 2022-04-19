#!/usr/bin/env python3

import os
import sys
import subprocess
import time

try:
    import yaml
except ImportError:
    #install the pyyaml module
    subprocess.call(["pip3", "install", "pyyaml"])
    import yaml
    #tell the user to restart the program
    print("Please restart the program")
    #exit the program
    sys.exit()

#try to import box module
try:
    from box import Box
except ImportError:
    #install the box module using "pip install python-box[all]~=6.0 --upgrade"
    subprocess.call(["pip3", "install", "python-box[all]~=6.0", "--upgrade"])
    from box import Box
    #tell the user to restart the program
    print("Please restart the program")
    #exit the program
    sys.exit()

#try to import the csv module
try:
    import csv
except ImportError:
    #install the csv module using "pip install csv"
    subprocess.call(["pip3", "install", "csv"])
    import csv
    #tell the user to restart the program
    print("Please restart the program")
    #exit the program
    sys.exit()

#try to import the tabulate module
try:
    import tabulate
except ImportError:
    #install the tabulate module using "pip install tabulate"
    subprocess.call(["pip3", "install", "tabulate"])
    import tabulate
    #tell the user to restart the program
    print("Please restart the program")
    #exit the program
    sys.exit()

#Try to import the rich module
try:
    from rich import print
except ImportError:
    #install the rich module using "pip install rich"
    subprocess.call(["pip3", "install", "rich"])
    from rich import print
    #tell the user to restart the program
    print("Please restart the program")
    #exit the program
    sys.exit()

salt_key = []
salt_hwaddr = []
salt_dict = {}  
salt_lines = []

try:
    import csv
except ImportError:
    subprocess.call([sys.executable, "-m", "pip", "install", "csv"])
    print("[!] The csv library is now installed")
    print("Please restart the program")
    time.sleep(3)
    sys.exit()

#This program takes the output of the salt "*" network.interfaces command turns it into a csv file

print('''[yellow]
 ┌────────────────────────────────────────────────────┐
 │  This program takes the output of a saltstack      │
 │  ```salt "*" network.interfaces``` command         │
 │  in yaml format and produces the salt minion name  │
 │  and hardware address as a csv file                │
 └────────────────────────────────────────────────────┘''')

#Delete the existing salt_hw.csv file if it exists
if os.path.exists("salt_hw.csv"):
    os.remove("salt_hw.csv")

#show the current directory and its contents
print("\nCurrent Directory: " + os.getcwd())
print("\nContents: ")
print(os.listdir())

#Ask the user for the output of the salt "*" network.interfaces command file,  if it does not exist ask again
while True:
    print("\nPlease enter the name of the yaml file that contains the salt network.interfaces output: ")
    salt_file = input("> ")
    if os.path.exists(salt_file):
        break
    else:
        print("\nThe file you entered does not exist, please try again")

#open the yanl file and split it into lines
with open(salt_file, 'r') as f:
    salt_lines = f.readlines()
    #remove intiial empty spaces in each line
    salt_lines = [x.strip() for x in salt_lines]


#Cycle through each line in the salt_lines list, if the line contains "-" and ends with ":" then it is a salt_key
for line in salt_lines:
    if line.endswith(":"):
        if "-" in line:
            salt_key.append(line)

#Cycle through each line in the salt_lines list, if the line starts with "hwaddr:" then add it to the list salt_hwaddr
for line in salt_lines:
    if line.startswith("hwaddr:"):
        salt_hwaddr.append(line)

#remove the "hwaddr:" from the salt_hwaddr list
salt_hwaddr = [x.replace("hwaddr: ", "") for x in salt_hwaddr]

#remove any element from the salt_key list that starts with "Intel"
salt_key = [x for x in salt_key if not x.startswith("Intel")]

#remove the ":" from the salt_key list
salt_key = [x.replace(":", "") for x in salt_key]

#So the salt_key list now contains the salt_keys and the salt_hwaddr list now contains the hardware addresses for those keys

#create a csv file with rows of salt_key and salt_hwaddr, naming it "salt_hw_2_csv.csv", if it already exists ask the user to delete it
if os.path.exists("salt_hw.csv"):
    print("\nThe file salt_hw.csv already exists, please delete it and try again")
    sys.exit()
else:
    with open("salt_hw.csv", "w") as f:
        writer = csv.writer(f)
        #add header row to csv file with salt_key and salt_hwaddr
        writer.writerow(["Computer Name", "Hardware Address"])
        writer.writerows(zip(salt_key, salt_hwaddr))

#remove the blank lines from the csv file
with open("salt_hw.csv", 'r') as f:
    lines = f.readlines()
    #remove the blank lines
    lines = [line for line in lines if line.strip()]
    #write the lines back to the file
    with open("salt_hw.csv", 'w') as f:
        f.writelines(lines)

#create an ascii table of the salt_key and salt_hwaddr lists
print("\n\nHere is the salt_key and salt_hwaddr list as an ascii table:\n")
#print the first 25 lines of the salt_key and salt_hwaddr lists, if the lists are longer say so
if len(salt_key) > 25:
    print(tabulate.tabulate(zip(salt_key[:25], salt_hwaddr[:25]), headers=["Computer Name", "Hardware Address"], tablefmt="grid"))
    print("\t...([italic]To see the rest of the list please see the [cyan]salt_hw.csv[/cyan] file[/italic])")
else:
    print(tabulate.tabulate(zip(salt_key, salt_hwaddr), headers=['Computer Name', 'Hardware Address']))

print("\n\n[yellow] ===[/yellow] Please see the created [cyan]salt_hw.csv[/cyan] for the computer name and hardware address of each salt minion [yellow]===[/yellow]\n")

#close all open files
f.close()

#Create a countdown timer that prints the time every second until the timer reaches 0
def countdown_timer():
    #set the timer to 10 seconds
    timer = 3
    #while loop to run the timer
    while timer > 0:
        #print the timer every second
        print(str(timer), end=" ".rstrip("\n"),)
        time.sleep(1)
        #decrement the timer by 1
        timer -= 1
    print("...", end="".rstrip("\n"))
#Say the to the user that program will exit in 3 seconds, call the countdown_timer function
print("\nProgram will exit in 3 seconds.")
countdown_timer()
sys.exit()
