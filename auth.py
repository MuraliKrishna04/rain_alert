import os
import requests
from twilio.rest import Client



endpoint ="https://api.openweathermap.org/data/2.5/forecast"
api_key = "d56dfbc7a4bf5dd7b80264923753ac76"
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

#twillo_key = DBFKF7WL9KVBAXF8NR163C8Y

#ATWILLO_KEY2 =D816BF76VX95NTZEZMAXGZ5X

parameters = {
    "lat": 17.385044,
    "lon": 78.486671,
    "appid": api_key,

}
response = requests.get(endpoint,params=parameters)
response.raise_for_status()
weather_data = response.json()
#print(weather_data["list"][0]["weather"])

will_rain = False

for hour_data in weather_data["list"]:
    condition_code = (hour_data["weather"][0]["id"])
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today, Remember to bring an umbrella ☔️",
        from_='whatsapp:+14155238886',
        to='whatsapp:+918106966566'
    )
    print(message.status)

