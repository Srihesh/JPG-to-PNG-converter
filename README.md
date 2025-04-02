# Image Converter to PNG Script

This Python script converts images from one format to PNG format in bulk.

## Features

- Converts all images in a specified folder to PNG format
- Creates output directory automatically if it doesn't exist
- Preserves original filenames (without extensions)
- Simple command-line interface

## Usage

Run the script from the command line with two arguments:
1. Input directory containing images to convert
2. Output directory for converted PNG files

```
python image_converter.py input_folder/ output_folder/
```

## Requirements

- Python 3.x
- Pillow library (install with `pip install Pillow`)

## How It Works

1. Takes input and output directories as command-line arguments
2. Creates the output directory if it doesn't exist
3. Processes each image in the input directory:
   - Opens the image using Pillow (PIL)
   - Extracts the clean filename (without extension)
   - Saves the image in PNG format to the output directory

## Notes

- The script will convert all files in the input directory that Pillow can recognize as images
- Output images will be in PNG format regardless of input format
- Handles basic error cases (like directory creation) but could be extended for more robust error handling

Perfect for batch converting images for web use or standardizing image formats in a project.
