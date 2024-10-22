import requests
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()

owm_endpoint = os.getenv('owm_endpoint')
api_key = os.getenv('api_key')
my_email = os.getenv('my_email')
my_password = os.getenv('gmail_password')


weather_params = {
    "lat": 40.772,
    "lon": -111.8711,
    # "lat": 42.4222,
    # "lon": -88.6137,
    "appid": api_key,
    "cnt": 4,
    "units": "imperial",
}
response = requests.get(owm_endpoint, params=weather_params)

# response = requests.get(url_5_day).json()
response.raise_for_status()
weather_data = response.json()

will_rain = False
for hour_data in weather_data["list"]:
    condition_codes = int(hour_data["weather"][0]["id"])
    if condition_codes < 700:
        will_rain = True

if will_rain:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="Jtester922@yahoo.com",
                            msg="Subject: Daily Forcast \n\n"
                                "It's going to rain. Bring an umbrella")
