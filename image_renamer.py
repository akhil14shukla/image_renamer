import os
import sys
import requests
from PIL import Image
import io
import base64

# Configuration: Update this if your LMStudio API endpoint is different
LMSTUDIO_API_URL = "http://127.0.0.1:1234/v1/chat/completions"
MODEL_NAME = "gemma-12b"

SUPPORTED_EXTENSIONS = {'.png', '.jpg', '.jpeg', '.bmp', '.gif'}

def get_image_files(directory):
    return [f for f in os.listdir(directory)
            if os.path.splitext(f)[1].lower() in SUPPORTED_EXTENSIONS]

def image_to_bytes(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def get_image_description(base64_image):
    # You may want to encode the image as base64 or use a captioning model first.
    # For now, we send a prompt to the LLM describing the image content.
    prompt = "Describe the content of this image in a short, descriptive filename (no spaces, use underscores, no extension):"
    # Optionally, you could use an image captioning model here and send the caption to the LLM.
    # For this example, we assume LMStudio can handle image bytes (update as needed).
    response = requests.post(
        LMSTUDIO_API_URL,
        json={
            "model": MODEL_NAME,
            "messages": [
                {"role": "system", "content": prompt},
                {"role": "user", "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image}"
                        }
                    }
                ]}
            ]
        }
    )
    response.raise_for_status()
    data = response.json()
    # Extract the filename suggestion from the LLM response
    return data['choices'][0]['message']['content'].strip()

def rename_images_in_directory(directory):
    image_files = get_image_files(directory)
    for filename in image_files:
        file_path = os.path.join(directory, filename)
        image_bytes = image_to_bytes(file_path)
        try:
            new_name = get_image_description(image_bytes)
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
