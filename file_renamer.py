"""File renamer: In this path, modify names of files after user navigates to a path and runs renamer.py"""

# Libraries
import os

# Get the current path
path = os.getcwd()

# Display current path to user
print(path)

# newFileName = Ask the user for the new file name (a naming pattern? prefix, suffix, etc)
newFileName = input("Enter the new file name: ")

# Display a confirmation message to the user that files will be renamed to newFileName
print("Files will be renamed to: " + newFileName)

# Walk through all files in directory
# Ignore subfolders !!!
nameList = os.listdir()
for file in nameList: 
    # Ignore hidden files
    if not file.startswith('.'):
        print(file)
        # Find file extension and add to newFileName
        ext = file.split('.')
        ext = '.' + ext[-1]
        rename = newFileName + ext
        print(rename)

"""
# Walk through path and rename all files to newFileName, ignoring the file extension in each name string
If item in path is a file
ext = get last n characters in name up to and including '.'
rename item with the new file name + ext
repeat for all items in path

#  Rename files
os.rename(file + newName for file in nameList)

# Inform the user that files have been renamed
Print "Files have been renamed"
"""