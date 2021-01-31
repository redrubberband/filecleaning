from modules import get_all_files, ffmpeg_compress

# Q: What does this file do?
# A: Converts source_formats to target_format (x265) using ffmpeg

#init ==============

source_formats = [
    'mp4',
    'avi',
    'webm',
]

target_format = 'mp4'

move_old_file_to_here   = "Old Files"
new_file_goes_here      = "Compressed"

#init end ==========

def main():
    ffmpeg_compress(source_formats, target_format, move_old_file_to_here, new_file_goes_here)
    print("Compression completed.")

if __name__ == "__main__":
    main()