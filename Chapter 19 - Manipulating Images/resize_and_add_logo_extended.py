#! python3
# resize_and_add_logo_extended.py - Resizes all images in current working directory to fit
# in a 300x300 square, and adds catlogo.png to the lower-right corner.

import os
from PIL import Image


def resize_and_add_logo():
    SQUARE_FIT_SIZE = 300
    LOGO_FILENAME = 'catlogo.png'

    logo_im = Image.open(LOGO_FILENAME)
    logo_width, logo_height = logo_im.size

    os.makedirs('withLogo', exist_ok=True)
    # Loop over all files in the working directory.
    for filename in os.listdir('.'):
        if not (filename.lower().endswith('.png') or filename.lower().endswith('.jpg')
                or filename.lower().endswith('.gif') or filename.lower().endswith('.bmp')) or filename == LOGO_FILENAME:
            continue    # skip non-image files and the logo file itself

        im = Image.open(filename)
        width, height = im.size
        if width < 2*logo_width or height < 2*logo_height:
            continue

        # Check if image needs to be resized.
        if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
            # Calculate the new width and height to resize to.
            if width > height:
                height = int((SQUARE_FIT_SIZE / width) * height)
                width = SQUARE_FIT_SIZE
            else:
                width = int((SQUARE_FIT_SIZE / height) * width)
                height = SQUARE_FIT_SIZE

            # Resize the image.
            print(f'Resizing {filename}...')
            im = im.resize((width, height))

        print(f'Adding logo to {filename}...')
        im.paste(logo_im, (width - logo_width, height - logo_height), logo_im)

        # Save changes.
        im.save(os.path.join('withLogo', filename))


if __name__ == '__main__':
    resize_and_add_logo()
