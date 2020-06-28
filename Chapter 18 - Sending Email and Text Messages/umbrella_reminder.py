# A program that checks whether it’s likely to rain today
# If so, the program will text you a reminder to pack an umbrella before leaving the house.

from twilio.rest import Client
import requests, bs4

# Preset values:
account_sid = 'ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
auth_token = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
my_number = '+___________'
twilio_number = '+___________'


def check_for_rain():
    # Replace the url here with the 10 day forecast from weather.com for your city
    url = 'https://weather.com/weather/tenday/'
    res = requests.get(url)
    res.raise_for_status()

    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    rain_probability_for_today_selector = '#WxuDailyCard-main-a43097e1-49d7-4df7-9d1a-334b29628263 > section > ' \
                                          'div._-_-components-src-organism-DailyForecast-DailyForecast' \
                                          '--DisclosureList--nosQS > details:nth-child(1) > div > ul:nth-child(2) > ' \
                                          'li:nth-child(2) > div > span._-_-components-src-molecule-DaypartDetails' \
                                          '-DetailsTable-DetailsTable--value--2YD0- '

    # Strip the '%' from the probability
    rain_probability_for_today = soup.select(rain_probability_for_today_selector)[0].text[:-1]
    if int(rain_probability_for_today) > 50:
        send_umbrella_reminder(rain_probability_for_today)


def send_umbrella_reminder(percentage):
    message = f'The change of rain today is {percentage}%. Be sure to pack your umbrella before leaving the house!'
    twilio_cli = Client(account_sid, auth_token)
    twilio_cli.messages.create(body=message, from_=twilio_number, to=my_number)


if __name__ == '__main__':
    check_for_rain()
