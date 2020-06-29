# A program that, given a .txt file path, goes through the text file line by line (will assume one guest per line)
# and uses the pillow module to create images for custom seating cards for each guest

import pyinputplus as pyip, os
from PIL import Image, ImageDraw, ImageFont


def create_custom_seating_cards(path):
    # make folder to store resulting images
    cards_folder = os.path.join(os.path.dirname(path), 'cards')
    os.makedirs(cards_folder, exist_ok=True)

    guest_list_file = open(path)
    guest_list_text = guest_list_file.read()
    guest_list = guest_list_text.split('\n')

    flower_img = Image.open('flower.png')

    # Define font to use for all guest cards
    fonts_folder = r'C:\Windows\Fonts'
    brush_script_font = ImageFont.truetype(os.path.join(fonts_folder, 'brushsci.ttf'), 24)

    for guest in guest_list:
        card = Image.new('RGBA', (288, 360), 'white')

        card.paste(flower_img, (10, 20))

        border = Image.new('RGBA', (293, 365), 'black')
        border.paste(card, (3, 3))

        draw = ImageDraw.Draw(border)
        draw.text((120, 100), guest, fill='red', font=brush_script_font)

        border.save(os.path.join(cards_folder, f'{guest}_seating_card.png'))

    guest_list_file.close()


if __name__ == '__main__':
    path_prompt = 'Please enter the full path to the guest list .txt file:\n'
    input_path = pyip.inputFilepath(prompt=path_prompt)
    create_custom_seating_cards(input_path)
