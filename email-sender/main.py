import os
import ssl
import datetime
import smtplib
from email.message import EmailMessage

email_sender = "romatimganov@gmail.com"
email_password = os.environ.get('EMAIL_PASS')
email_receiver = "rt.hnya@gmail.com"

# print(email_password)
# for name, value in os.environ.items():
#     print("{0}: {1}".format(name, value))

subject = 'SPY GAME ' + str(f'{datetime.datetime.today()}')
print(subject)
# to do
body = '''place or YOU'RE THE SPY'''

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())
