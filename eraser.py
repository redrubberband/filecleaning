from modules import erase, get_all_files
from pathlib import Path
import os
def main():
    all_files = Path.cwd().rglob(".")
    for file in all_files:
        print(file, bool(file.is_file), bool(file.parent == Path.cwd()))

if __name__ == "__main__":
    main()
    