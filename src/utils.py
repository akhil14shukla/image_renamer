import os
import base64
from src.constants import SUPPORTED_EXTENSIONS
from PIL import Image
import io
import numpy as np
import hashlib


def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


def get_image_files(directory):
    return [
        f
        for f in os.listdir(directory)
        if os.path.splitext(f)[1].lower() in SUPPORTED_EXTENSIONS
    ]


def image_to_bytes(image_path, size=(224, 224)):
    # get extension from image_path
    ext = os.path.splitext(image_path)[1].lower()[1:]
    ext_map = {
        "jpg": "JPEG",
        "jpeg": "JPEG",
        "png": "PNG",
        "gif": "GIF",
        "bmp": "BMP",
        "tiff": "TIFF",
    }
    ext = ext_map.get(ext, "JPEG")  # Default to JPEG if not found
    with open(image_path, "rb") as image_file:
        img = Image.open(image_path).convert("RGB").resize(size)
        buffer = io.BytesIO()
        img.save(buffer, format=ext, quality=80)
        return base64.b64encode(buffer.getvalue()).decode("utf-8")


def get_image_cache_key(base64_image: str) -> str:
    return hashlib.sha256(base64_image.encode("utf-8")).hexdigest()
