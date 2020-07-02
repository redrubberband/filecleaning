from pathlib import Path

def getAllFiles():
    print("Scanning directory...")
    currentDir = Path.cwd().iterdir()                   #currentDir is getting all the files in the current directory. NOT RECURSIVE.
    return currentDir