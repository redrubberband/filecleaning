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

#init end ==========

def main():
    handbrake_convert(source_formats, target_format)
    print("Conversion completed.")

if __name__ == "__main__":
    main()