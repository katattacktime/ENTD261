# *****************************************************************
#
#   Script Name:    Recursive File Filter
#   Author:         Kat Ayer
#   Due Date:       March 11, 2023
#   University:     American Public University
#
# *****************************************************************

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Used a combination of OS and pathlib to not have to deal with the OS string issue. Pathlib let me use path objects
# instead which helped simplify some finagling.
#
# For inputs, instead of requiring a user to pre-enter via a command line argument, I opted for the input function,
# which also allowed text to accompany and clarify prompts, and overall, in my opinion, leads to more user-friendly
# scripts.
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#import needed modules
import os
import pathlib


# Should ask what the path to the folder to check
source = input('Enter the full folder path. (e.g. C:\\Users\\user\\Documents)\n')


# Validate folder exists, if it doesn't, throw a specific error
if os.path.exists(source) == False:
    print('Path does not exist. Double check path spelling, and try again.')
    exit()

# Checks if the user-entered path is a file
if os.path.isfile(source) == True:
    print('Path routes to file. Remove the last section, and try again.')
    exit()


# Should ask if the user wants to search for greater than or less than a certain ntumber
sizeLimit = input('\nIf you want to filter the files by size, enter a number here (in kB). \nThe next step will allow you to select if you want files that are greater than, less than, or otherwise.\nElse, enter 0 and choose greater than on the next step to search for all.\n\n Enter a file size limit (in kB):\n')


# Verify that input is a valid, positive number. If function throws a ValueError, display a certain message.
# Try-Except assignment requirement
while True:
    try:
        int(sizeLimit)
        break
    except ValueError:
        print('\n Input is not a number. Try again.')
        exit()


# Checks to ensure that the number entered is not negative
if sizeLimit.startswith('-'):
    print('\nNumber cannot be negative. Try again.')
    exit()


# String to integer conversion
limit = int(sizeLimit)


# Ask for the operator to filter
operator = input(
    '\nSelect one by typing the symbol in brackets and pressing Enter: \n - Greater than [>] \n - Less than [<] \n - Equal to [=] \n - Equal or greater than [>=] \n - Equal or less than [<=] \n - Not Equal [=/=]\n')


# Turn source into path object instead of string
pathSource = pathlib.Path(source)


# Each of the following functions are the same except their comparison operator on the 4th line.
# Greater than
if operator == str('>'):
    def get_items(root: pathlib.Path):
        for item in root.iterdir():
            if os.path.getsize(item) > limit*1024:
                print(f"{item}\n - {'Folder' if item.is_dir() else 'File'}\n - {os.path.getsize(item)/1024} kB\n")
                if item.is_dir():  # Recursively looks inside any directories it encounters
                    yield from get_items(item)
    for item in get_items(pathSource):
        print(item)


# Less Than
elif operator == str('<'):
    def get_items1(root: pathlib.Path):
        for item in root.iterdir():
            if os.path.getsize(item) < limit*1024:
                print(
                    f"{item}\n - {'Folder' if item.is_dir() else 'File'}\n - {os.path.getsize(item)/1024} kB\n")
                if item.is_dir():  # Recursively looks inside any directories it encounters
                    yield from get_items1(item)
    for item in get_items1(pathSource):
        print(item)


# Equal To
elif operator == str('='):
    def get_items2(root: pathlib.Path):
        for item in root.iterdir():
            if os.path.getsize(item) == limit*1024:
                print(
                    f"{item}\n - {'Folder' if item.is_dir() else 'File'}\n - {os.path.getsize(item)/1024} kB\n")
                if item.is_dir():  # Recursively looks inside any directories it encounters
                    yield from get_items2(item)
    for item in get_items2(pathSource):
        print(item)


# Less Than or Equal To
elif operator == str('<='):
    def get_items3(root: pathlib.Path):
        for item in root.iterdir():
            if os.path.getsize(item) <= limit*1024:
                print(
                    f"{item}\n - {'Folder' if item.is_dir() else 'File'}\n - {os.path.getsize(item)/1024} kB\n")
                if item.is_dir(): # Recursively looks inside any directories it encounters
                    yield from get_items3(item)
    for item in get_items3(pathSource):
        print(item)


# Greater Than or Equal To
elif operator == str('>='):
    def get_items4(root: pathlib.Path):
        for item in root.iterdir():
            if os.path.getsize(item) >= limit*1024:
                print(
                    f"{item}\n - {'Folder' if item.is_dir() else 'File'}\n - {os.path.getsize(item)/1024} kB\n")
                if item.is_dir():  # Recursively looks inside any directories it encounters
                    yield from get_items4(item)
    for item in get_items4(pathSource):
        print(item)


# Not Equal
elif operator == str('=/='):
    def get_items5(root: pathlib.Path):
        for item in root.iterdir():
            if os.path.getsize(item) != limit*1024:
                print(
                    f"{item}\n - {'Folder' if item.is_dir() else 'File'}\n - {os.path.getsize(item)/1024} kB\n")
                if item.is_dir():  # Recursively looks inside any directories it encounters
                    yield from get_items5(item)
    for item in get_items5(pathSource):
        print(item)


# If user input does not match any of the above, print this:
else:
    print('Please only type one of the symbols in the brackets. No spaces. Try again.')
    exit()
