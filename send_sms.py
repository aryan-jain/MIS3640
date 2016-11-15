# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "ACe0d1afd10e3e9bca43c9f5d373a6cf96"
auth_token = "d319ccef503533b150e35ba0630e51a8"
client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(to="+16173206890", from_="+15555555555",
                                 body="Hello there!")
