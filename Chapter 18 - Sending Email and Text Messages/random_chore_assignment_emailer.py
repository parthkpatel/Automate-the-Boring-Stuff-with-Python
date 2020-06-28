# A program that takes a list of people’s email addresses and a list of chores that need to be done
# and randomly assigns chores to people.

import pyinputplus as pyip, random, smtplib


def email_chores(chores, email_addresses, login_email, login_password):
    smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
    smtp_obj.ehlo()
    smtp_obj.starttls()
    smtp_obj.login(login_email, login_password)

    for email_address in email_addresses:
        random_chore = random.choice(chores)
        chores.remove(random_chore)
        print(f'Sending chore {random_chore} to the email {email_address}...')
        smtp_obj.sendmail(login_email, email_address,
                          'Subject: Your Chore\n\nHello,\nHere is your chore: ' + random_chore)
    smtp_obj.quit()


if __name__ == '__main__':
    chores_string = pyip.inputStr(prompt='Please enter a comma-separated list of chores:\n')
    email_addresses_string = pyip.inputStr(prompt='Please enter a comma-separated list of emails:\n')
    email = pyip.inputEmail(prompt='Please enter the email address to use to send the chores:\n')
    password = pyip.inputStr(prompt='Please enter your email password:\n')

    chores_list = chores_string.split(',')
    email_addresses_list = email_addresses_string.split(',')
    email_chores(chores_list, email_addresses_list, email, password)
