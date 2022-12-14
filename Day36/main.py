import requests
from datetime import datetime, timezone, timedelta

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = ""

START_TIME = "04:30:00"
END_TIME = "20:00:00"


    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

# https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo
parameter = {
    "function": "TIME_SERIES_INTRADAY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
    "interval": "30min"
}

response = requests.get(STOCK_ENDPOINT, params=parameter)
response.raise_for_status()
print(response)
data = response.json()
print(data)
time_series = data["Time Series (30min)"]

"""
cur_date = datetime.now(timezone.utc).strftime('%Y-%m-%d')
today_first_time = f"{cur_date} {START_TIME}"
yesterday_date = (datetime.now(timezone.utc) - timedelta(1)).strftime('%Y-%m-%d')
yesterday_last_time = f"{yesterday_date} {END_TIME}"
"""
# following code use data of yesterday and the day before yesterday
cur_date = (datetime.now(timezone.utc) - timedelta(1)).strftime('%Y-%m-%d')
today_first_time = f"{cur_date} {START_TIME}"
yesterday_date = (datetime.now(timezone.utc) - timedelta(2)).strftime('%Y-%m-%d')
yesterday_last_time = f"{yesterday_date} {END_TIME}"

print(today_first_time)
print(yesterday_last_time)
today_first_data = time_series[today_first_time]
yesterday_last_data = time_series[yesterday_last_time]
print(today_first_data)
print(yesterday_last_data)

print(f"today open value - yesterday close value = {float(today_first_data['1. open']) - float(yesterday_last_data['4. close'])}")

#TODO 2. - Get the day before yesterday's closing stock price

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: ????2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: ????5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

