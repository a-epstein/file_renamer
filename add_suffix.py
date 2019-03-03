"""Adds a suffix to every file in folder"""

import os

def getSuffix():
    # Get user input for the suffix to be entered
    suffix = input("Enter the suffix that will be appended to each file name: ")
    return suffix

def getExt(filename = ''):
    # Split the extension from the file name
    ext = filename.split('.')
    ext = '.' + ext[-1]
    return ext

def getFilename(filename = ''):
    # Split the filename from the extension
    filename = filename.split('.')
    filename = filename[0]
    return filename

def addSuffix(filename= ''):
    # Get filepath
    path = os.getcwd()

    # Walk through all files in directory, ignore hidden files and subfolders
    nameList = os.listdir(path)
    for name in nameList:
        if not name.startswith('.') and not os.path.isdir(name):

            # Rename the file
            newName = getFilename(name) + getSuffix() + getExt(name)
            os.rename(name, newName)
            return name + " has been renamed to " + newName
    
addSuffix()


"""
file = 'cool.jpg'
print("Add the suffix to filenames: " + getSuffix())
print("The filename is: " + getFilename(file))
print("The file extension is: " + getExt(file))
"""