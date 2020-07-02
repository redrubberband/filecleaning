from scandir import getAllFiles
from pathlib import Path
import shutil

#init ==================================================================
currentDir = Path.cwd()

IMAGE_EXTENSIONS = (
    '.png',   
    '.jpg', 
    '.jpeg'
)

GIF_EXTENSIONS = (
    '.gif'
)

VIDEO_EXTENSIONS = (
    '.webm', 
    '.avi', 
    '.mp4', 
    '.mkv'
)

#static functions, replacement for constants since python has none.
def IMG_FOLDER():
    return "J"

def GIF_FOLDER():
    return "G"

def VIDEO_FOLDER():
    return "WM"

#init end ==============================================================

def move(filename, filetype):
    #man:
    #send filename -> Path
    #send filetype -> String/Char -> ex: "J"

    currentDir.joinpath(filetype).mkdir(exist_ok=True)                  #create the directory if missing
    newPath = currentDir.joinpath(filetype)                             #creates new path as target for shutil
    shutil.move(str(filename), str(newPath))                            #somehow shutil only accepts str, but the docs said it can accept Path. Strange that it doesn't work here.

def main():
    filesInDir = getAllFiles()

    print("Moving files...")
    for file in filesInDir:
        if file.is_file():
            if str(file).lower().endswith(IMAGE_EXTENSIONS):
                move(file, IMG_FOLDER())
            elif str(file).lower().endswith(GIF_EXTENSIONS):
                move(file, GIF_FOLDER())
            elif str(file).lower().endswith(VIDEO_EXTENSIONS):
                move(file, VIDEO_FOLDER())

    print("Separation completed.")

main()