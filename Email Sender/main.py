from email.message import EmailMessage
import ssl
import smtplib
from empw import password

# Define the email endpoints.
email_sender='ilyes.berrian@gmail.com'
email_password= password
email_receiver='yanoder965@izeao.com'

# Fill the message object elements.
subject='Email Sender'
body='''
Hey,
If you receive this message then Email Sender project is working well!!
Thanks.
'''
msg=EmailMessage()
msg['From']=email_sender
msg['To']=email_receiver
msg['Subject']=subject
msg.set_content(body)

# The variable is to store SSL protocol.
context=ssl.create_default_context()

# Sending Email Procedures. 
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    #Authentication Checking.
    smtp.login(email_sender, password)
    # Sending the email.
    smtp.send_message(msg)