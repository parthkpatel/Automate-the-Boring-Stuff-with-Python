# A program that goes through every folder on your hard drive and finds potential photo folders.

import os
from PIL import Image, UnidentifiedImageError


def find_photo_folders():
    for foldername, subfolders, filenames in os.walk('C:\\'):
        num_photo_files = 0
        num_non_photo_files = 0
        for filename in filenames:
            # Check if file extension isn't .png or .jpg.
            if not (filename.lower().endswith('.png') or filename.lower().endswith('.jpg')):
                num_non_photo_files += 1
                continue    # skip to next filename

            # Open image file using Pillow.
            try:
                image = Image.open(os.path.join(foldername, filename))
            except UnidentifiedImageError:
                continue
            width, height = image.size

            # Check if width & height are larger than 500.
            if width > 500 and height > 500:
                # Image is large enough to be considered a photo.
                num_photo_files += 1
            else:
                # Image is too small to be a photo.
                num_non_photo_files += 1

        # If more than half of files were photos,
        # print the absolute path of the folder.
        if num_photo_files > num_non_photo_files:
            print(os.path.abspath(foldername))


if __name__ == '__main__':
    find_photo_folders()
