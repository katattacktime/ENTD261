# *****************************************************************
#
#   Script Name:    
#   Author:         Kat Ayer
#   Due Date:       March 11, 2023
#   University:     American Public University
#
# *****************************************************************

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# DELETE ME BEFORE TURNING IN
#Create a Python script that takes two parameters to do the following:-
#   1) List all files names, size, date created in the given folder
#       - Parameter1 = Root Folder name
#       - Parameter2= File size >>> to filter file size ( you can do =, > or <) it is up to you, or a range.
#   2) The script should check and validate the folder name, and the size
#   3) The script should loop until find all files greater than the specified size in all the sub-folders
#   4) Use try-exception block (Make sure that the error messages do not reveal any of the application code)
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import glob
import os
import pathlib


# Should ask what the path to the folder to check
source = input('Enter the full folder path. (e.g. C:\\Users\\user\\Documents)\n')


#Validate folder exists, if it doesn't, throw a specific error
if os.path.exists(source) == False:
    print('Path does not exist. Double check path spelling, and try again.')
    exit()

if os.path.isfile(source) == True:
    print('Path routes to file. Remove the last section, and try again.')
    exit()


#Should ask if the user wants to search for greater than or less than a certain ntumber
sizeLimit = input('\nIf you want to filter the files by size, enter a number here (in kB). \nThe next step will allow you to select if you want files that are greater than, less than, or otherwise.\nElse, enter 0 and choose greater than on the next step to search for all.\n\n Enter a file size limit (in kB):\n')

# Verify that input is a valid, positive number
while True:
    try:
        int(sizeLimit)
        break
    except ValueError:
        print('\n Input is not a number. Try again.')
        exit()

if sizeLimit.startswith('-'):
    print('\nNumber cannot be negative. Try again.')
    exit()

limit = int(sizeLimit)

# Ask for the operator
operator = input(
    '\nSelect one by typing the symbol in brackets and pressing Enter: \n - Greater than [>] \n - Less than [<] \n - Equal to [=] \n - Equal or greater than [>=] \n - Equal or less than [<=] \n - Not Equal [=/=]\n')

pathSource = pathlib.Path(source)

def get_items(root: pathlib.Path):
    for item in root.iterdir():
        if os.path.getsize(item) > limit*1024:
            print(f"{item}\n - {'Folder' if item.is_dir() else 'File'}\n - {os.path.getsize(item)/1024} kB\n")
            if item.is_dir():
                yield from get_items(item)

if operator == str('>'):
    get_items(pathSource)
#    for item in pathSource.iterdir():
#        if os.path.getsize(item) > limit*1024:
#            print(f"{item}\n - {'Folder' if item.is_dir() else 'File'}\n - {os.path.getsize(item)/1024} kB\n")
#            if item.is_dir():

elif operator == str('<'):
    filter(lambda x: os.path.getsize < sizeLimit(1024),
           [os.path.join(source, x) for x in pathList])

elif operator == str('='):
    filter(lambda x: os.path.getsize == sizeLimit(1024),
           [os.path.join(source, x) for x in pathList])

elif operator == str('<='):
    filter(lambda x: os.path.getsize <= sizeLimit(1024),
           [os.path.join(source, x) for x in pathList])

elif operator == str('>='):
    filter(lambda x: os.path.getsize >= sizeLimit(1024),
           [os.path.join(source, x) for x in pathList])

elif operator == str('=/='):
    filter(lambda x: os.path.getsize != sizeLimit(1024),
           [os.path.join(source, x) for x in pathList])

else:
    print('Please only type one of the symbols in the brackets. No spaces. Try again.')
    exit()
# Search and loop until all files are found


# Loading animation?

