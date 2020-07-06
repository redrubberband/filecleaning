from pathlib import Path
import shutil

currentDir = Path.cwd()
def move(file, newfoldername):
    #man:
    #send file -> Path
    #send newfoldername -> String/Char -> ex: "J"

    currentDir.joinpath(newfoldername).mkdir(exist_ok=True)         #create the directory if missing
    newPath = currentDir.joinpath(newfoldername)                    #creates new path as target for shutil
    shutil.move(str(file), str(newPath))                            #somehow shutil only accepts str, but the docs said it can accept Path. Strange that it doesn't work here.

def getAllFiles():
    print("Scanning directory...")
    return currentDir.iterdir()                                     #currentDir is getting all the files in the current directory. NOT RECURSIVE.