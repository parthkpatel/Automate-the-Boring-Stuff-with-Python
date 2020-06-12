# A program that, given the URL of a web page, will attempt to download every linked page on the page.
# The program flags any pages that have a 404 “Not Found” status code and print them out as broken links

import requests, bs4, os
from urllib.parse import urlparse
import pyinputplus as pyip


def download_linked_pages(url):
    main_url_res = requests.get(url)
    if not is_link_verified(main_url_res, url):
        return
    else:
        soup = bs4.BeautifulSoup(main_url_res.text, 'html.parser')
        links = soup.select('a[href]')
        counter = 0
        for link in links:
            unformatted_url = link.get('href')
            if unformatted_url.startswith('http'):
                formatted_url = unformatted_url
                counter += 1
            elif unformatted_url.startswith(('#', '../', '.')):
                formatted_url = f'{os.path.dirname(url)}/{unformatted_url}'
                counter += 1
            elif unformatted_url.startswith('/'):
                parsed_url = urlparse(url)
                formatted_url = f'{parsed_url.scheme}://{parsed_url.hostname}/{unformatted_url}'
                counter += 1

            url_res = requests.get(formatted_url)
            is_link_verified(url_res, formatted_url)


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
    input_url = pyip.inputURL(prompt="Please enter the full URL to download the linked pages from:\n")
    download_linked_pages(input_url)
