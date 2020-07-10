# filecleaning

...is a personal project of file management.

## Warning

This program was made in Windows so some commands may not work in another OS.

Especially moveaudio.py (which in turn, also scanaudio.py), as both used the commands for windows command prompt. You might be able to change a few lines to make it work in Linux-based OS, though.

## Requirement(s)

* You need to have ffmpeg, ffplay, and ffprobe in the same folder as this project.
* Python ver. 3.8

## Usage

Just use it inside your terminal inside the target folder by calling python.

## FUNCTIONS:

* modules.py

    The toolbox for every single python code I use here. Not runnable on it's own.

* scanaudio.py
    
    Scans the current directory using ffmpeg to detect audio levels.

* moveaudio.py

    Uses the logfile created by scanaudio.py to detect and separate any audio files to its corresponding folder.

* movedupes.py

    A simple duplicate detection for my other code, SankakuKeybinds. This code will move any file with "(" to the "Duplicates" folder. The reason why I'm using "(" is because most browsers simply added numbers to a duplicate file when downloaded again.

* renamefiles.py

    A file renamer for files downloaded from hanime.tv to make it easier on the eyes. Changes "-" into space and removes any suffix like v1x etc.

* separatefiles.py

    Separates all file in the folder to its corresponding subfolder. Currently only separates images, gifs, and video files. The video files can be later separated again by moveaudio.py by cd-ing into the folder first.