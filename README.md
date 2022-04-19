# SaltStack-MAC2CSV:

Takes the yaml formatted output of the saltstack command ```salt -G os:windows network.interfaces``` and turns it into a csv file for easy review within a spreadsheet

## Why?
* Having a list of the salt names correlated to hardware addresses in a spreadsheet allows one to quickly search a network for a specific resource

## Dependencies
* Requires python3.x
* Attempts to install the csv, tabular & rich libraries if not already installed


## Input of the yaml file:<br>
![image](https://user-images.githubusercontent.com/48565067/163863260-705b6f67-377e-4092-8e5e-7888d9dc112e.png)

## Screen Output:<br>
![image](https://user-images.githubusercontent.com/48565067/163861368-2bb6b511-e1b4-493a-9bea-676be2dd2475.png)
![image](https://user-images.githubusercontent.com/48565067/163862051-c00fcde6-55f1-4771-a6c4-73d88ae1243e.png)

## Output of the ```salt_hw.csv``` file:
* Outputs a csv file with the computer name, and hardware address of all the devices seen in the yaml file
