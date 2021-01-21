import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

fromaddr = "email_address_of_the_sender"
toaddr = "email_address_of_the_receiver"

# MIMEMultipart
msg = MIMEMultipart()

# senders email address
msg['From'] = "shesiva@gmail.com"

# receivers email address
msg['To'] = "shesiva@gmail.com"

# the subject of mail
msg['Subject'] = "subject_of_the_mail"

# the body of the mail
body = "body_of_the_mail"

# creates SMTP session
email = smtplib.SMTP('smtp.gmail.com', 587)

# TLS for security
email.starttls()

# authentication
email.login(fromaddr, "Password_of_the_sender")

# Converts the Multipart msg into a string
message = msg.as_string()

# sending the mail
email.sendmail(fromaddr, toaddr, message)

# terminating the session
s.quit()
