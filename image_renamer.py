import os
import sys

from src.system_functions import rename_images_in_directory


def main():
    if len(sys.argv) != 2:
        print("Usage: python image_renamer.py /path/to/image/folder")
        sys.exit(1)
    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"Directory '{directory}' does not exist.")
        sys.exit(1)
    rename_images_in_directory(directory)


if __name__ == "__main__":
    main()
