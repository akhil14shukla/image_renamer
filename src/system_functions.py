## Main script to rename images in a directory using LLM-generated names

from src.utils import get_image_files, image_to_bytes
from src.image_functions import get_image_new_name_from_llm
from src.prompts import IMAGE_RENAME_PROMPT
import os


def rename_images_in_directory(directory):
    image_files = get_image_files(directory)
    for filename in image_files:
        file_path = os.path.join(directory, filename)
        image_bytes = image_to_bytes(file_path)
        try:
            new_name = get_image_new_name_from_llm(image_bytes, IMAGE_RENAME_PROMPT)
            ext = os.path.splitext(filename)[1].lower()
            new_filename = f"{new_name}{ext}"
            new_path = os.path.join(directory, new_filename)
            if new_filename != filename:
                os.rename(file_path, new_path)
                print(f"Renamed '{filename}' to '{new_filename}'")
            else:
                print(f"No change for '{filename}'")
        except Exception as e:
            print(f"Failed to rename '{filename}': {e}")
