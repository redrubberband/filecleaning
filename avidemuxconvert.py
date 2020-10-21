from modules import get_all_files, avidemux_convert

#init ==============

source_formats = (
    'ts'
)

target_format = 'mp4'

#init end ==========

def main():
    avidemux_convert(source_formats, target_format)
    print("Conversion completed.")

if __name__ == "__main__":
    main()