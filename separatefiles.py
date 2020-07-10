from modules import get_all_files, move

#init ==================================================================

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

def main():
    files_in_dir = get_all_files()
    
    for file in files_in_dir:
        if file.is_file():
            if str(file).lower().endswith(IMAGE_EXTENSIONS):
                move(file, IMG_FOLDER())
            elif str(file).lower().endswith(GIF_EXTENSIONS):
                move(file, GIF_FOLDER())
            elif str(file).lower().endswith(VIDEO_EXTENSIONS):
                move(file, VIDEO_FOLDER())

    print("Separation completed.")

if __name__ == "__main__":
    main()