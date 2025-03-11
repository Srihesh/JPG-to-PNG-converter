import sys
import os
from PIL import Image

#using sys module to enter arguments in terminal
image_folder = sys.argv[1]
output_folder = sys.argv[2]

#check if new folder exists, if not create one (using os or pathlib)
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

#loop through images
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_name = os.path.splitext(filename)[0]
    img.save(f'{output_folder}{clean_name}.png','png')
    print('Done!')


