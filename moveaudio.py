import time
from pathlib import Path
from modules import ffmpeg_scan, move, erase, get_all_files

# Initialization
currentDir = Path.cwd()

has_audio_list  = []
no_audio_list   = []

LOGFILE_NAME            = "log.txt"
AUDIO_DIRECTORY_NAME    = "hasAudio"
NO_AUDIO_DIRECTORY_NAME = "noAudio"

logfile = currentDir.joinpath(LOGFILE_NAME)

FILE_DETECTOR_STRING    = "[Parsed"                                     # Line used to mark that a file has any audio at all

supported_formats = [
    "mp4",
    "webm",
    "avi",
    "mkv",
    "m4v"
]

def scan_directory():
    with logfile.open("r", encoding ="utf-8") as file:
        
        logfile_lines = file.readlines()
        file_has_audio = False
        
        for line in logfile_lines:
            
            if (FILE_DETECTOR_STRING in line):                          # Detects whether the current file has audio or not
                decibel_value = line.split(" ")
                decibel_value = float(decibel_value[4])                 # 4 is the value where the dB value is stored
                
                if (decibel_value > -80):                               # Usually, if it has -91.0 dB as the value then it has no audio. But 80 is chosen, just in case.
                    file_has_audio = True
                else:
                    pass
                continue

            filename = get_filename(line)

            if (file_has_audio):
                file_has_audio = False                                  # Return it to false to continue scanning other files
                has_audio_list.append(filename)                         # Appends the file to the list which contain files with audio
                continue

            else:
                no_audio_list.append(filename)                          # Appends the file to the list which contain files without audio

def move_all():                                                         # Move the files to its corresponding folder

    for filename in has_audio_list:
        file = currentDir.joinpath(filename)
        move(file, AUDIO_DIRECTORY_NAME)
    
    for filename in no_audio_list:
        file = currentDir.joinpath(filename)
        move(file, NO_AUDIO_DIRECTORY_NAME)   

def get_filename(filepath):
    return Path(filepath).name.rstrip(" \n")

def main():
    
    print("Checking existing logfile for removal...")
    if logfile.exists():
        print("Logfile detected. Removing...")
        erase(logfile)
    else:
        print("No logfile found.")

    print("Scanning files and creating logfile...")
    is_file_available = ffmpeg_scan(supported_formats)
    if (not is_file_available):                                         # Exits the app if there is no file returned by ffmpeg_scan
        print("Exiting...")
        exit()
    time.sleep(2)                                                       # Sleep to let the system rest for a bit in case there's any lag/delay

    print("Checking audio availability...")
    scan_directory()

    print("Separating and moving files...")
    move_all()

    print("Removing logfile...")
    erase(logfile)

    print("Operation success!") 

if __name__ == "__main__":
    main()
