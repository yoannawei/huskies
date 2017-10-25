import os

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC4cd69b0b35b83cf384f4eefce61ecdac"
# Your Auth Token from twilio.com/console
auth_token  = "fc8b3207974c483f52ed27f707557937"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+12487192862",
    from_="+12018066758",
    body="Hello my puppy! This is kitty's husky app. Reminder to pick up puppy meal.",
    media_url=['http://cdn1-www.dogtime.com/assets/uploads/2016/09/husky-5.jpg'])

print(message.sid)

