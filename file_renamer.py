"""Docstring"""

# Libraries
import os

# Assign list of all files in directory to nameList
nameList = os.listdir()
print(nameList)

# String you want to add
newName = "cool"

#  Rename files
os.rename(file + newName for file in nameList)
