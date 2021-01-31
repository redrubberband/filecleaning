from modules import get_all_files, handbrake_convert

# Q: What does this file do?
# A: Converts source_formats to target_format using handbrake

#init ==============

source_formats = [
    'mp4',
    'avi',
    'webm',
]

target_format = 'm4v'

move_old_file_to_here   = "Old Files"
new_file_goes_here      = "Converted"

#init end ==========

def main():
    handbrake_convert(source_formats, target_format, move_old_file_to_here, new_file_goes_here)
    print("Conversion completed.")

if __name__ == "__main__":
    main()