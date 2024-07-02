import os
import requests
from twilio.rest import Client



endpoint = os.environ['ENDPOINT_URL']
api_key = os.environ['ENDPOINT_API_KEY']
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']

#twillo_key = DBFKF7WL9KVBAXF8NR163C8Y

#ATWILLO_KEY2 =D816BF76VX95NTZEZMAXGZ5X

parameters = {
    "lat": 16.560909,
    "lon": 81.519638,
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

