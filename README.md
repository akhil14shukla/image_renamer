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

## Notes
- The script assumes LMStudio exposes a local API endpoint for LLM inference.
- Update the API endpoint in the script if needed.
