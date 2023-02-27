# Programme Develop by Induwara Uthsara 
# **** Github = https://github.com/induwarauthsara/
# **** Web = http://induwara.rf.gd
# Date : 28/02/2023
# Copyright (c) 2023
# All rights reserved.

from os import system, name
from time import sleep
def clear():
   # for windows
   if name == 'nt':
      _ = system('cls')
   # for mac and linux
   else:
      _ = system('clear')

clear()

print ("#################################\nStudent's House Finder Programme\nMRC Inter-House Sportmeet")
print ('Developed by Induwara Uthsara\n#################################\n')
while True:
    index = input('Enter Index No. : ')
    if not (index.isnumeric()):
        print("Invalid Index Number \n")
        continue
    else:
        index = int(index)
        
    h_no = index%6
    if(h_no == 0):
        h = 'Wishwa'
    elif(h_no == 1):
        h = 'Gagana'
    elif(h_no == 2):
        h = 'Sayura'
    elif(h_no == 3):
        h = 'Derana'
    elif(h_no == 4):
        h = 'Soorya'
    elif(h_no == 5):
        h = 'Pawana'
    else:
        h = 'ERROR !!!'
    
    print('Your House is - '+ h)
    print("")
    again = input("Do You Want to Run Programme Again ? (y/n): ")
    print("")
    if(again == 'n'):
        break 
    
print("Good Bye...!\n")
print("Github url: https://github.com/induwarauthsara/Find-House-in-Sportmeet")
