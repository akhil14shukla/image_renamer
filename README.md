# ImageRenamer

This Python project reads image files (such as screenshots) from a directory, analyzes their content, and renames them based on the content. It uses the Gemma 12B LLM model (via the local LMStudio app) to generate descriptive names for the images.

## Features

- Reads all image files from a specified directory
- Analyzes image content
- Uses Gemma 12B LLM (via LMStudio) to suggest new filenames
- Renames images accordingly

## Requirements

- Python 3.8+
- LMStudio app running locally with Gemma 12B model
- Required Python packages (see below)

## Setup

1. Ensure LMStudio is running locally and the Gemma 12B model is loaded.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the script:
   ```bash
   python image_renamer.py /path/to/image/folder
   ```

## How it works

1. Place your screenshots or image files in a folder (e.g., `~/Desktop/screenshots`).
2. Run the script on that folder:
   ```bash
   python image_renamer.py ~/Desktop/screenshots
   ```
3. The script will:
   - Read each image file in the folder
   - Send the image to the Gemma 12B LLM via LMStudio
   - Receive a descriptive filename suggestion (e.g., `error_dialog_july_2025.png`)
   - Rename the image file accordingly

### Example

Suppose your folder contains:

```
Screenshot 2025-06-30 at 10.00.00.png
Screenshot 2025-06-30 at 10.01.00.png
```

After running the script, you might get:

```
error_dialog_july_2025.png
settings_menu_dark_mode.png
```

### Experimental: Image Clustering

This project also includes an **experimental feature** for clustering images based on their content embeddings. Instead of renaming, the script can group similar images together using KMeans clustering on LLM-generated embeddings.

To try clustering, edit `image_renamer.py` to call `cluster_images_by_embeddings(directory)` instead of `rename_images_in_directory(directory)`. The script will print out which cluster each image belongs to. You can adjust the number of clusters in the code as needed.

#### Example output

```
Image 'Screenshot 2025-06-30 at 10.00.00.png' is in cluster 0
Image 'Screenshot 2025-06-30 at 10.01.00.png' is in cluster 1
```

### How this helps

- **Organization:** Your screenshots and images will have meaningful, searchable filenames.
- **Automation:** No need to manually review and rename each file.
- **Productivity:** Quickly find images by their content, not by generic timestamps.

## Notes

- The script assumes LMStudio exposes a local API endpoint for LLM inference.
- Update the API endpoint in the script if needed.
