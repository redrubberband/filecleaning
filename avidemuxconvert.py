from modules import get_all_files, avidemux_convert, get_time

# Q: What does this file do?
# A: Converts source_formats to target_format using avidemux

#init ==============

source_formats = [
    'ts'
]

target_format = 'mp4'

#init end ==========

def main():
    start_time = get_time()
    avidemux_convert(source_formats, target_format)
    finish_time = get_time()
    minutes_elapsed = round((finish_time - start_time).total_seconds(), 2)
    print("Conversion completed.")
    print("Start: %s" %start_time)
    print("Finished: %s" %finish_time)
    print("Time elapsed: %s" %minutes_elapsed)

if __name__ == "__main__":
    main()