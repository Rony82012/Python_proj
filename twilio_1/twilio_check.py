from twilio.rest import Client

#account SID and auth token from Twilio login
account_sid = "AC6f8f75aa0f5d3a6cdab4985ec47ad6e1"
auth_token = "f6adefffca14a1147c724a608a23152b"
client = Client(account_sid,auth_token)


message = client.messages.create(to="+14156760814", from_="+14158438345",
                                 body="Hey MAD, Life ain't so BAD. Only you can ADD, from when you HAD. You'll be GLAD, coz i'm RAD. Dinkchak")

