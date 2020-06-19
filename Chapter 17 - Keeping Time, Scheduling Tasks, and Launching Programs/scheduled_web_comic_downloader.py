# A program that checks the websites of 2 web comics and automatically downloads the images,
# if the comic was updated since the program’s last visit.
# This program uses a separate thread to download comics from the different sites


import requests, os, bs4, time, sys, shelve, threading

comics_data = [['http://xkcd.com', '#comic img', 'http:', 'xkcd_last_image_downloaded'],
               ['https://www.exocomics.com/', '.comic > img', '', 'exocomics_last_image_downloaded']
               ]


def comic_downloader(url, comic_element_selector, comic_image_url_prefix, last_image_downloaded_filename):
    # opens main page of comic, checks the comic img source, if it is different from what
    # is in database, downloads it

    print(f'Opening {url}')
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    comic_element = soup.select(comic_element_selector)
    if not comic_element:
        print(f'No comic on found at {url}.')
        sys.exit()
    else:
        comic_img_url = comic_element[0].get('src')
        full_comic_url = comic_image_url_prefix + comic_img_url

    if f'{last_image_downloaded_filename}.txt' in os.listdir():
        last_image_downloaded_file = open(f'{last_image_downloaded_filename}.txt')
        if last_image_downloaded_file.read() == full_comic_url:
            print('The comic has not changed from the last download.')
            last_image_downloaded_file.close()
            sys.exit()

    print(f'Downloading comic {os.path.basename(full_comic_url)}')
    res = requests.get(full_comic_url)
    res.raise_for_status()
    image_file = open(os.path.join('Comics', os.path.basename(full_comic_url)), 'wb')
    for chunk in res.iter_content(100000):
        image_file.write(chunk)
    image_file.close()

    print('Storing the newly downloaded comic information.')
    last_image_downloaded_file = open(last_image_downloaded_filename + '.txt', 'w')
    last_image_downloaded_file.write(full_comic_url)
    last_image_downloaded_file.close()

    print('End of thread.')


if __name__ == '__main__':
    print('Beginning program.')

    # creates folder to store comics there
    print('Creating folder to place the downloaded comics, if the folder does not already exist.')
    os.makedirs('Comics', exist_ok=True)

    # Only proceed if it has been longer than 24 hours since the last run
    if 'time_data.dat' in os.listdir():
        shelve_file = shelve.open('run_time_data')
        last_run_time = shelve_file['last_run_time']
        print('Checking when the program was opened last time.')
        if time.time() - last_run_time < 86400:
            print('This program was opened less than 24 hours ago.')
            shelve_file.close()
            sys.exit()

    download_threads = []

    comics_data = [['http://xkcd.com', '#comic img', 'http:', 'xkcd_data'],
                   ['https://www.exocomics.com/', '.comic > img', '', 'exocomics_data']
                   ]

    for comic_data in comics_data:
        download_thread = threading.Thread(target=comic_downloader, args=comic_data)
        download_threads.append(download_thread)
        download_thread.start()

    # Wait for all threads to end.
    for download_thread in download_threads:
        download_thread.join()

    print('Changing time data in database')
    shelve_file = shelve.open('run_time_data')
    last_run_time = time.time()
    shelve_file['last_run_time'] = last_run_time
    shelve_file.close()
    print('End of program')
