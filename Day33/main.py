import requests
from datetime import datetime, timezone
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import time

MY_LAT = 37.566536  # my latitude
MY_LONG = 126.977966  # my longitude
MY_PASSWORD = ""

# Get iss position
def is_iss_overhead():
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_long = float(data['iss_position']['longitude'])
    iss_lat = float(data['iss_position']['latitude'])

    if -5 <= (MY_LAT - iss_long) <= 5 and -5 <= (MY_LONG - iss_long) <= 5:
        return True
    else:
        return False


def is_night():
    parameter = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameter)
    response.raise_for_status()
    data = response.json()['results']
    sunrise = data['sunrise']
    sunset = data['sunset']
    sunrise_hour = int(sunrise.split("T")[1].split(":")[0])
    sunset_hour = int(sunset.split("T")[1].split(":")[0])
    # sunrise/sunset time got from API have time based on England. But datetime.now() have local(Korean) time.
    # I got an answer(analysis) about it from Q & A. The timezone I've got from the API is GMT or UTC not England time.
    # And Korean timezone is UTC + 9.

    # Two solution
    # 1. use offset
    # sunrise_hour = (sunrise_hour + 9) % 24
    # sunset_hour = (sunset_hour + 9) % 24
    # cur_time = datetime.now()

    # 2. getting current time with UTC timezone.
    cur_time = datetime.now(timezone.utc)

    # print(data)
    # print(sunrise_hour)
    # print(sunset_hour)
    # print(cur_time)

    if cur_time.hour > sunset_hour or cur_time.hour < sunrise_hour:
        return True
    else:
        return False


#For debugging
# is_iss_overhead()
# is_night()

# Send mail if the above condition is fulfilled.
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        print("ISS is overhead and It's night currently.")
        my_email = "acezero3@naver.com"
        my_password = MY_PASSWORD
        to_email = my_email
        smtp_address = "smtp.naver.com"

        message = MIMEMultipart()
        message['Subject'] = "Lookup and find ISS!!"
        message['From'] = "acezero3@naver.com"
        message['To'] = to_email

        content = """
            <html>
            <body>
                <h2>{msg_body}</h2>
            </body>
            </html>
        """.format(
            msg_body = "Lookup and find ISS!!"
        )

        mimetext = MIMEText(content,'html')
        message.attach(mimetext)

        connect = smtplib.SMTP(smtp_address)
        connect.starttls()
        connect.login(user=my_email, password=my_password)
        connect.sendmail(message['From'], to_email, message.as_string())
        connect.close()

