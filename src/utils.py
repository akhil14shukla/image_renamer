import os
import base64
from src.constants import SUPPORTED_EXTENSIONS


def get_image_files(directory):
    return [
        f
        for f in os.listdir(directory)
        if os.path.splitext(f)[1].lower() in SUPPORTED_EXTENSIONS
    ]


def image_to_bytes(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")
