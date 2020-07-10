from modules import get_all_files, move
from string import digits

DUPLICATE_DIRECTORY = "Duplicates"

extensions_to_check = [
    "(",
    ")"
]

def main():
    
    files_in_dir = get_all_files()
    isDuplicateFound = False
    
    print("Checking for duplicates...")
    for file in files_in_dir:
        if file.is_file():
            filename = file.stem
            if any(extension in filename for extension in extensions_to_check):
                move(file, DUPLICATE_DIRECTORY)
                isDuplicateFound = True

    if (isDuplicateFound):
        print("Duplicates found and successfuly moved!")
    else:
        print("No duplicate found!")

if __name__ == "__main__":
    main()