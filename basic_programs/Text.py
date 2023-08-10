#twillio for text voice or audio
from twilio.rest import Client

account_sid = 'ACa0909188bdfb531dc9c6b91cb3f89d25'
auth_token = '3b0e42da86266d97fbc8542acdf55aa1'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+15188643786',
  body='T',
  to='+919324526912'
)
# +15188643786

print(message.sid)