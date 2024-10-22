import smtplib

import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
news_api_key = "0f9c65ad91eb43bf822ec55c5ec18982"
# stock_api_key = "BSIHP3Z296MAGW4J"
# stock_api_key = "FDBADCLOZ3VFSPUN"
stock_api_key = "ZM6JFTCD7W0YVQDN"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
my_email = "billtester511@gmail.com"
my_password = "pidt zwsx fdvt ybxs"

# r = requests.get(STOCK_ENDPOINT)
# print(r.json())

    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": stock_api_key

}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
# print(response.json())
data = response.json()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(f"Yesterday's closing price: {yesterday_closing_price}")

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = day_before_yesterday_data["4. close"]
print(f"2 days ago closing price: {day_before_yesterday_closing_price}")

difference = float(yesterday_closing_price) - float(day_before_yesterday_closing_price)
up_down = None
if difference > 0:
    up_down = "⮝"
else:
    up_down = "⮟"

diff_percent = round((difference / float(yesterday_closing_price)) * 100)
print(difference)
print(diff_percent)

## Testing email part
# diff_percent = 1
# difference = 2
# up_down = None
# if difference > 0:
#     up_down = "⮝"
# else:
#     up_down = "⮟"

if abs(diff_percent) > .05:
    news_params = {
        "apiKey": news_api_key,
        "qInTitle": COMPANY_NAME,
    }
    news_response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]
    # print(articles)

    three_articles = articles[:3]
    # print(three_articles)

    formated_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \nBrief: {article['description']}. \nURL: {article['url']}" for  article in three_articles]
    # clean_data = formated_articles.replace('…', '...')

    for article in formated_articles:
        message = f"Subject:{COMPANY_NAME}Stock News\n\n{article}"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(my_email, my_password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="Jtester922@yahoo.com",
                msg=message.encode('utf-8')
            )









