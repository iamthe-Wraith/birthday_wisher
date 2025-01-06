import smtplib
import os
import pandas as pd
import datetime as dt
from dotenv import load_dotenv
load_dotenv()

smtp_email = os.getenv('SMTP_EMAIL')
smtp_token = os.getenv('SMTP_TOKEN')
smtp_host = os.getenv('SMTP_HOST')
smtp_port = os.getenv('SMTP_PORT')

df = pd.read_csv("birthdays.csv")
now = dt.datetime.now()

def send_email(email, subject, message):
    # use `with` to ensure the connection is closed after use
    with smtplib.SMTP(smtp_host, smtp_port) as connection:
        connection.starttls() # IMPORTANT: secures the connection with tls
        connection.login(user=smtp_email, password=smtp_token)
        connection.sendmail(
            from_addr=smtp_email,
            to_addrs=email,
            msg=f"Subject:{subject}\n\n{message}"
        )

for index, row in df.iterrows():
    date_object = dt.datetime.strptime(row["birthday"], "%b %d, %Y")
    if date_object.month == now.month and date_object.day == now.day:
        send_email(row["email"], "Happy Birthday!", f"Happy Birthday {row['name']}!")
