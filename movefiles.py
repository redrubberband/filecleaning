#fileversion = v0.2

#imports
#import shutil
import time
from pathlib import Path
import scanaudio

#customization
filepath = "log.txt"                                                     #where is the file located? relative to execution folder, because it'll get converted to absolute path down the line
trashline = '"=========================================="'.strip()       #what line is not needed in the master list file? (this var can be empty)
detectorline = "[Parsed"                                                 #what line marks the file in the master list file? (ffmpeg shows [Parsed ... before the actual chosen file shows up)
supportedFormats = [                                                     #what files are supported here?
    "mp4",
    "webm",
    "avi",
    "mkv"
]

#init
hasAudioList = []
noAudioList = []
isValid = False                                                         #boolean marker to show if a correct file has been found
currentDir = str(Path.cwd())+"\\"
filepath = Path(currentDir + filepath)                                  #wraps the complete file path

def scan(isValid):
    with filepath.open("r", encoding ="utf-8") as file:
        lines = file.readlines()

        for line in lines:                                              #remove trash separator to uniformize all inputs
            if (trashline in line):
                lines.remove(line)
                pass                                                    #let it run even if there's no trashline

        for line in lines:
            
            if (detectorline in line):                                  #put this check before the isValid check to prevent breaking the code (broken loop)
                dB_read = line.split(" ")
                dB_read = float(dB_read[4])                             #4 is the value where the dB value is stored
                
                if (dB_read > -80):                                     #usually, if it has -91.0 dB as the value then it has no audio. 80 is chosen just in case.
                    isValid = True
                else:
                    pass
                
                continue

            filename = cut(line)

            if (isValid):
                isValid = False                                         #return it to false to continue scanning other files
                hasAudioList.append(filename)                           #appends the file to the hasAudioList list
                continue

            else:
                noAudioList.append(filename)                            #appends the file to the noAudioList list

def move():
    Path(currentDir + "hasAudio\\").mkdir(exist_ok=True)                #create the directory if missing
    Path(currentDir + "noAudio\\").mkdir(exist_ok=True)

    for file in hasAudioList:
        Path(file).rename("hasAudio/"+file)
    
    for file in noAudioList:
        Path(file).rename("noAudio/"+file)

def remove(logfile):
    logfile.unlink()
    

def cut(fullpath):
    currentFilename = fullpath.split("\\")                              #split each folders
    folderCounter = len(currentFilename)-1                              #how deep is the file in the path?
    currentFilename = currentFilename[folderCounter]                    #filename is n-th folder deep

    currentFilename = currentFilename.split(" \n")[0]                   #split the remaining string and get the original filename
    return currentFilename

def printlist(listName):                                                #debugging function, not used in actual program
    if (listName.lower() == "hasaudiolist"):
        print(hasAudioList)
    else:
        print(noAudioList)

def main():
    print("Removing logfile if it already existed...")
    try:
        remove(filepath)
    except:
        pass

    print("Scanning files and creating logfile...")
    isFileAvailable = scanaudio.scan(supportedFormats)                  #boolean value
    if (not isFileAvailable):                                           #checks if the scanfiles.py returns any file at all
        print("Exiting...")
        exit()
    time.sleep(3)                                                       #sleep to let the system rest for a bit in case there's any lag/delay

    print("Checking audio availability...")
    scan(isValid)

    print("Separating and moving files...")
    move()

    print("Removing logfile...")
    remove(filepath)

    print("Operation success!") 

    #===log testkit===
    #scan(isValid)
    #printlist("hasAudioList")
    #print("===")
    #printlist("noAudioList")

#=======call the main function==========
main()
