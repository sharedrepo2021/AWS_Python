import smtplib


FROM = 'chandrasusmita69@gmail.com'
TO = ["dipan.saha@gmail.com"]
SUBJECT = input("Subject of the Email:: ")
TEXT = input("Write the msg:: ")

# Prepare actual message

message = """
From: %s
To: %s
Subject: %s

%s
""" % (FROM, ", ".join(TO), SUBJECT, TEXT)

# Send the mail

server = smtplib.SMTP('smtp.gmail.com', 587)

server.ehlo()
server.starttls()
server.login('pythondev2021@gmail.com', 'pass4python')

server.sendmail(FROM, TO, message)
server.close()

print('Message Delivered successfully!')