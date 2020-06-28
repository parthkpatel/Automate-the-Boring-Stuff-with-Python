# A program that scans through your email account,
# finds all the unsubscribe links in all your emails, and automatically opens them in a browser.

import pyinputplus as pyip, imapclient, imaplib, bs4, pyzmail, webbrowser


def open_unsubscribe_links(email, password):
    imaplib._MAXLINE = 10000000
    imap_obj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
    imap_obj.login(email, password)
    imap_obj.select_folder('INBOX', readonly=True)
    unique_ids = imap_obj.search(['ALL'])

    links_to_unsubscribe_from = []

    for unique_id in unique_ids:
        raw_message = imap_obj.fetch([unique_id], ['BODY[]', 'FLAGS'])
        message = pyzmail.PyzMessage.factory(raw_message[unique_id][b'BODY[]'])
        if message.html_part is None:
            continue
        message_html = message.html_part.get_payload().decode(message.html_part.charset)
        soup = bs4.BeautifulSoup(message_html, 'html.parser')
        link_elems = soup.select('a')
        for element in link_elems:
            if 'unsubscribe' in str(element).lower():
                links_to_unsubscribe_from.append(element.get('href'))

    imap_obj.logout()

    for link in links_to_unsubscribe_from:
        print(f'Opening {link}...')
        webbrowser.open(link)


if __name__ == '__main__':
    input_email = pyip.inputEmail(prompt='Please enter the email address:\n')
    input_password = pyip.inputStr(prompt='Please enter your email password:\n')

    open_unsubscribe_links(input_email, input_password)
