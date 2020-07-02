from pathlib import Path
import os

#init
files = []
def scan(supportedFormats):
    for format in supportedFormats:                                         #scans the folder for any supported file
        currentDir = Path.cwd().glob("*." + format)
        for filename in currentDir:
            if filename.is_file():
                files.append(filename)

    if not files:
        print("There is no supported file in the folder.")
        return False                                                        #returns false if there is no supported file in the folder

    for file in files:
        os.system("ffmpeg -hide_banner -i \"" +                             #uses ffmpeg (volumedetect feature) to detect whether an audio track exists or not
                str(file) + 
                "\" -af volumedetect -vn -f null - 2>&1 | findstr mean_volume >> log.txt")
        os.system("ECHO " + str(file) + " >> log.txt")                      #prints the file list to a logfile
    
    return True                                                             #returns true if there is at least ONE supported file in the folder