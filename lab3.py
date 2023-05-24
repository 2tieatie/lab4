import os


def print_dir_size(files_format: str, directory: str = '.'):
    directory = directory.replace('"', '')
    files_format = files_format.replace('*', '')
    print(files_format)
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory '{directory}' does not exist.")
    total_size = 0
    file_count = 0
    for dirpath, dirnames, filenames in os.walk(directory):
        for file in filenames:
            if file.endswith(files_format):
                filepath = os.path.join(dirpath, file)
                file_size = os.path.getsize(filepath)
                total_size += file_size
                file_count += 1
                print(f"{filepath} ({file_size} bytes)")
    print(f"Total size: {total_size} bytes")
    print(f"Total files: {file_count}")


if __name__ == "__main__":
    directory = input('Enter directory (format "dir\\dir\\dir\\dir"): ')
    files_format = input('Enter files format (format *.exe, just push Enter if you want to count all the files): ')
    print_dir_size(files_format, directory)
