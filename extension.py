#author : Lakshmi A G
#21 Jan 2023

extDict = {"py" : "Python" , "c" : "C" , "cs" : "Visual C#" , "java" : "Java" , "cpp" : "C++"}
file= input("Enter Filename: ")
f = file.split(".")     #separating the file name and the extension
ext = f[-1]             #taking the last element i.e., extension for comparison
if (ext in extDict):
    print("The extension of the file is :" , extDict[ext])
else:
    print("The given extension not in dictionary")
