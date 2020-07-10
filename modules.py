from pathlib import Path
import shutil
import os

currentDir = Path.cwd()
DUPLICATE_FOLDER_NAME = "Duplicates"
NAME_BEFORE_REMOVAL = "regret"

def erase(file):

    # Manual:
    # Renames the file before it's deleted.

    dead_file = currentDir.joinpath(NAME_BEFORE_REMOVAL)
    retry_count = 2
    for _ in range(retry_count):
        try:
            "Removing file..."
            shutil.move(str(file), str(dead_file))
            dead_file.unlink()
            break
        except BaseException as e:
            print(e)
            "Retrying once again..."
            dead_file.unlink()
    pass

def move(file, NEW_FOLDER_NAME):
    print("Moving files...")

    # Manual:
    # "file" type is Path
    # "newfoldername" type is String/Char -> ex: "J"

    currentDir.joinpath(NEW_FOLDER_NAME).mkdir(exist_ok=True)                 #create the directory if missing
    newPath = currentDir.joinpath(NEW_FOLDER_NAME)                            #creates new path as target for shutil
    
    has_duplicate_file = False

    for oldfile in newPath.iterdir():

        if (oldfile.name == file.name):

            print("Duplicate detected in " + NEW_FOLDER_NAME + "! Moving file for manual inspection to /Duplicates")
            
            duplicate_folder = currentDir.joinpath(DUPLICATE_FOLDER_NAME)
            duplicate_folder.mkdir(exist_ok=True)

            duplicate_path = duplicate_folder.joinpath(NEW_FOLDER_NAME)
            duplicate_path.mkdir(exist_ok=True)

            shutil.move(str(file), str(duplicate_path))
            has_duplicate_file = True
            
            break

    if not has_duplicate_file:
        shutil.move(str(file), str(newPath))                                # According to docs, shutil *should* be able to receive Path. But this one doesn't work without conversion to str(), strange.

def get_all_files():
    print("Scanning directory...")
    return currentDir.iterdir()                                             # Return all the files in the current directory. NOT RECURSIVE.

def ffmpeg_scan(supported_formats):                                         # WARNING: CREATES A LOGFILE. REMEMBER TO INCLUDE A  REMOVAL FUNCTION IN YOUR CODE.
    
    files = []
    
    for format in supported_formats:                                        # Scans the folder for files with supported file format
        currentDir = Path.cwd().glob("*." + format)
        for filename in currentDir:
            if filename.is_file():
                files.append(filename)

    if not files:
        print("There is no supported file in the folder.")
        return False                                                        # Returns false if there is no supported file in the folder

    for file in files:
        os.system("ffmpeg -hide_banner -i \"" +                             # Uses ffmpeg (volumedetect feature) to detect whether an audio track exists or not
                str(file) + 
                "\" -af volumedetect -vn -f null - 2>&1 | findstr mean_volume >> log.txt")
        os.system("ECHO " + str(file) + " >> log.txt")                      # Prints the file list to a logfile
    
    return True                                                             # Returns true if there is at least ONE supported file in the folder