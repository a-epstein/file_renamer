"""File renamer: In this path, modify names of files after user navigates to a path and runs renamer.py"""

# Libraries
import os

# Get the current path
path = os.getcwd()

# Display current path to user
print(path)

# User input
# newFileName = Ask the user for the new file name (a naming pattern? prefix, suffix, etc)
newFileName = input("Enter the new file name: ")

# Display a confirmation message to the user that files will be renamed to newFileName
print("Files will be renamed to: " + newFileName)

"""
# Walk through path and rename all files to newFileName, ignoring the last 4 characters in each name string
If item in path is a file
ext = get last 4 characters in name
rename item with the new file name + ext
repeat for all items in path

#  Rename files
os.rename(file + newName for file in nameList)

# Inform the user that files have been renamed
Print "Files have been renamed"
"""








