from modules import get_all_files, handbrake_convert, get_time

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
    start_time = get_time()
    handbrake_convert(source_formats, target_format, move_old_file_to_here, new_file_goes_here)
    finish_time = get_time()
    minutes_elapsed = round((finish_time - start_time).total_seconds(), 2)
    print("Conversion completed.")
    print("Start: %s" %start_time)
    print("Finished: %s" %finish_time)
    print("Time elapsed: %s" %minutes_elapsed)

if __name__ == "__main__":
    main()