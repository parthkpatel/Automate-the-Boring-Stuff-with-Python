# A program that goes to Imgur, searches for a category of photos,
# and then downloads a specified number of the resulting images

import requests, bs4, os
from urllib.parse import urlparse
import pyinputplus as pyip


def image_site_download(search_phrase, num_images, path_to_save):
    os.makedirs(path_to_save, exist_ok=True)

    request_url = f'https://imgur.com/search?q={search_phrase}'
    main_url_res = requests.get(request_url)
    if not is_link_verified(main_url_res, request_url):
        return
    else:
        soup = bs4.BeautifulSoup(main_url_res.text, 'html.parser')
        images = soup.select('.image-list-link img')
        total_images_to_download = min(num_images, len(images))

        for i in range(total_images_to_download):
            image_src = images[i].get('src')
            split_path = os.path.splitext(image_src)
            full_image_url = f'https:{split_path[0][:-1]}{split_path[1]}'

            image_response = requests.get(full_image_url)
            if is_link_verified(image_response, full_image_url) is True:
                image_name = os.path.basename(full_image_url)
                image_file = open(os.path.join(os.path.abspath(path_to_save), image_name), 'wb')
                print(f'Downloading Image {i+1} out of {total_images_to_download}: {image_name}')
                for chunk in image_response.iter_content(100000):
                    image_file.write(chunk)
                image_file.close()


def is_link_verified(response, url):
    try:
        response.raise_for_status()
        return True
    except Exception as exc:
        if response.status_code == 404:
            print(f'404 Error: The link {url} is a broken link.')
        else:
            print(f'There was a problem: {exc}')
        return False


if __name__ == '__main__':
    phrase = pyip.inputStr(prompt="Enter the search phrase for the images you would like to download from Imgur:\n")
    num_images = pyip.inputInt(prompt="Enter the number of images you would like to download, provided that there: "
                                      "are that many images to download (Program Maximum = 100):\n", max=100, min=0)
    path_to_save = pyip.inputFilepath(prompt='Please enter the full path to the folder '
                                             'where you would like to store the images:\n')
    image_site_download(phrase, num_images, path_to_save)
