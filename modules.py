from pathlib import Path
import shutil
import os
import subprocess

currentDir              = Path.cwd()
DUPLICATE_FOLDER_NAME   = "Duplicates"
NAME_BEFORE_REMOVAL     = "regret"

avidemux_path           = r'C:\Program Files\Avidemux 2.7 VC++ 64bits\avidemux.exe'
handbrake_path          = r'D:\Portable Softwares\HandBrakeCLI-1.3.3-win-x86_64\HandBrakeCLI.exe'

def erase(file):

    # Renames the file before it's deleted.

    dead_file = currentDir.joinpath(NAME_BEFORE_REMOVAL)

    if dead_file.exists():
        "Duplicate detected! Removing the duplicate first..."
        dead_file.unlink()

    print("Removing file...")
    try:
        shutil.move(str(file), str(dead_file))
        dead_file.unlink()
    except BaseException as e:
        print(e)

def move(file, NEW_FOLDER_NAME):
    print("Moving files...")

    # Manual:
    # "file" type is Path
    # "newfoldername" type is String/Char -> ex: "J"

    target_path = currentDir.joinpath(NEW_FOLDER_NAME)                      # Creates new path as target for shutil
    target_path.mkdir(exist_ok=True)                                        # Creates the directory if missing
        
    if(target_path.joinpath(file.name).exists()):
        print("Duplicate detected in " + NEW_FOLDER_NAME + \
            "! Moving file for manual inspection to /Duplicates")

        duplicate_folder = currentDir.joinpath(DUPLICATE_FOLDER_NAME)       # Creates a "Duplocates" folder
        duplicate_folder.mkdir(exist_ok=True)

        # Temporarily disabled because it creates unnecessary clutter
        #duplicate_path = duplicate_folder.joinpath(NEW_FOLDER_NAME)         # Creates a folder for their own file types
        #duplicate_path.mkdir(exist_ok=True)

        shutil.move(str(file), str(duplicate_folder))

    else:

        shutil.move(str(file), str(target_path))                            # According to docs, shutil *should* be able to receive Path. But this one doesn't work without conversion to str(), strange. 

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
        # I tried fixing this with subprocess but I don't understand how. For now, at least.
        os.system("ffmpeg -hide_banner -i \"" +                             # Uses ffmpeg (volumedetect feature) to detect whether an audio track exists or not
                str(file) + 
                "\" -af volumedetect -vn -f null - 2>&1 | findstr mean_volume >> log.txt")
        os.system("ECHO " + str(file) + " >> log.txt")                      # Prints the file list to a logfile
    
    return True                                                             # Returns true if there is at least ONE supported file in the folder

def avidemux_convert(source_formats, target_format):

    video_codec      = "Xvid"
    audio_codec      = "mp3"

    files = []
    
    for format in source_formats:                                            # Scans the folder for files with supported file format
        currentDir = Path.cwd().glob("*." + format)
        for filename in currentDir:
            if filename.is_file():
                files.append(filename)

    if not files:
        print("There is no supported file in the folder.")
        return False                                                        # Returns false if there is no supported file in the folder

    for file in files:

        target_filename = str(file.stem) + "." + target_format              # subprocess can only work without space and extra concatenation, so merge your filenames here.
        
        subprocess.run([str(avidemux_path), 
                    "--video-codec", video_codec, 
                    "--audio-codec", audio_codec, 
                    "--force-alt-h264",
                    "--load", file.name,
                    "--save", target_filename,
                    "--quit"
                    ])

        # Quick and dirty way. DO NOT REMOVE. This might work as a backup.
        #console_command = "cmd /c \"\"" + str(avidemux_path) + "\" --video-codec " + video_codec + " --audio-codec " + audio_codec + " --force-alt-h264 --load \"" + file.name + "\" --save \"" + str(file.stem) + "." + target_format + "\" --quit\""
        #os.system(console_command)
    return True  

def mass_move_files(source_formats, target_directory):

    files = []

    for format in source_formats:                                            # Scans the folder for files with supported file format
        currentDir = Path.cwd().glob("*." + format)
        for filename in currentDir:
            if filename.is_file():
                files.append(filename)


    if not files:
        print("There is no supported file in the folder.")
        return False                                                        # Returns false if there is no supported file in the folder

    for file in files:
        move(file, target_directory)

def handbrake_convert(source_formats, target_format, move_old_file_to_here, new_file_goes_here):

    preset_location = r'handbrake_compressor_preset.json'
    # This is a bit messy, but because the preset is in the same folder as the script,
    # I need to access __file__'s location to get it.
    handbrake_preset_location = Path(__file__).parent.joinpath(preset_location) 
    preset_name = "Compressor"
    # I already made a preset file.
    # If you want to use this feature and don't have any custom preset,
    # and then create a custom one.   

    # If you don't want to, just remove the "-Z" line below.
    # (Better yet, why not use HandBrakeCLI.exe directly?)

    files = []
    
    for format in source_formats:                                            # Scans the folder for files with supported file format
        currentDir = Path.cwd().glob("*." + format)
        for filename in currentDir:
            if filename.is_file():
                files.append(filename)

    if not files:
        print("There is no supported file in the folder.")
        return False                                                        # Returns false if there is no supported file in the folder

    for file in files:

        target_filename = str(file.stem) + "." + target_format              # subprocess can only work without space and extra concatenation, so merge your filenames here.
        
        subprocess.run([str(handbrake_path), 
                    "--preset-import-file", handbrake_preset_location,
                    "-Z", preset_name,
                    "-i", file.name,
                    "-o", target_filename
                    ])

        move(file, move_old_file_to_here)
        move(Path(target_filename), new_file_goes_here)

    return True  

def ffmpeg_compress(source_formats, target_format, move_old_file_to_here, new_file_goes_here):

    files = []
    
    for format in source_formats:                                            # Scans the folder for files with supported file format
        currentDir = Path.cwd().glob("*." + format)
        for filename in currentDir:
            if filename.is_file():
                files.append(filename)

    if not files:
        print("There is no supported file in the folder.")
        return False                                                        # Returns false if there is no supported file in the folder

    for file in files:

        target_filename = str(file.stem) + "_compressed." + target_format              # subprocess can only work without space and extra concatenation, so merge your filenames here.
        
        subprocess.run(["ffmpeg", 
                    "-hide_banner",
                    "-i", file.name,
                    "-c:v", "libx265",
                    target_filename,
                    ])

        move(file, move_old_file_to_here)
        move(Path(target_filename), new_file_goes_here)

    return True  