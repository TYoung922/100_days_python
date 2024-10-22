import smtplib
import datetime as dt
import random

my_email = "billtester511@gmail.com"
my_password = "pidt zwsx fdvt ybxs"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 2:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    print(quote)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        # msg = msg.encode('ascii', 'ignore').decode('ascii')
        connection.starttls()
        connection.login(my_email, my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="Jtester922@yahoo.com",
            msg=f"Subject:Wednesday Motivation\n\n{quote}")