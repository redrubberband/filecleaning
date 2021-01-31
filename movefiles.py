from modules import mass_move_files, move
import sys

TARGET_DIRECTORY = "moved_here"

source_formats = []

if len(sys.argv) <= 1:
    source_formats.extend(['ts', 'idx2'])
else:
    sys.argv.pop(0) # removes the file name from args
    for args in sys.argv:
        source_formats.append(args)


def main():
    mass_move_files(source_formats, TARGET_DIRECTORY)

if __name__ == "__main__":
    main()