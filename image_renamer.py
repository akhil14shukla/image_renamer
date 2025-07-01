import os
import sys

from src.system_functions import (
    rename_images_in_directory,
)
from src.image_functions import cluster_images_by_embeddings


def main():
    if len(sys.argv) != 2:
        print("Usage: python image_renamer.py /path/to/image/folder")
        sys.exit(1)
    directory = sys.argv[1]
    if not os.path.isdir(directory):
        print(f"Directory '{directory}' does not exist.")
        sys.exit(1)
    rename_images_in_directory(directory)
    # cluster_images_by_embeddings(directory)


if __name__ == "__main__":
    main()
