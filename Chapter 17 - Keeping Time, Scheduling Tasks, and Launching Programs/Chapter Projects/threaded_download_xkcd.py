#! python3
# threaded_download_xkcd.py - Downloads XKCD comics using multiple threads.

import requests, os, bs4, threading

os.makedirs('xkcd', exist_ok=True)  # store comics in ./xkcd


def download_xkcd(start_comic, end_comic):
    for url_number in range(start_comic, end_comic):
        # Download the page.
        print(f'Downloading page https://xkcd.com/{url_number}...')
        res = requests.get(f'https://xkcd.com/{url_number}')
        res.raise_for_status()

        soup = bs4.BeautifulSoup(res.text, 'html.parser')

        # Find the URL of the comic image.
        comic_elem = soup.select('#comic img')
        if not comic_elem:
            print('Could not find comic image.')
        else:
            comic_url = comic_elem[0].get('src')
            # Download the image.
            print(f'Downloading image {comic_url}...')
            res = requests.get(f'https:{comic_url}')
            res.raise_for_status()

            # Save the image to ./xkcd.
            image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
            for chunk in res.iter_content(100000):
                image_file.write(chunk)
            image_file.close()


# Create and start the Thread objects.
download_threads = []  # a list of all the Thread objects
for i in range(0, 140, 10):  # loops 14 times, creates 14 threads
    start = i
    end = i + 9
    if start == 0:
        start = 1  # There is no comic 0, so set it to 1.
    download_thread = threading.Thread(target=download_xkcd, args=(start, end))
    download_threads.append(download_thread)
    download_thread.start()

# Wait for all threads to end.
for downloadThread in download_threads:
    downloadThread.join()
print('Done.')
