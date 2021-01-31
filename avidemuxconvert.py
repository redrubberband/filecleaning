from modules import get_all_files, avidemux_convert

# Q: What does this file do?
# A: Converts source_formats to target_format using avidemux

#init ==============

source_formats = [
    'ts'
]

target_format = 'mp4'

#init end ==========

def main():
    avidemux_convert(source_formats, target_format)
    print("Conversion completed.")

if __name__ == "__main__":
    main()