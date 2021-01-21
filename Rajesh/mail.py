import smtplib
from email.message import EmailMessage


msg = EmailMessage()

recipient_id = input("Enter the Recipient mail ID : ")

msg['To'] = recipient_id
msg['Subject'] = input("Enter the subject for this mail : ")
msg['From'] = 'pythondev2021@gmail.com'

msg.set_content(input("Enter the message : "))

mail = smtplib.SMTP('smtp.gmail.com', 587)
mail.ehlo()
mail.starttls()
mail.login('pythondev2021@gmail.com', 'pass4python')

mail.sendmail('pythondev2021@gmail.com', recipient_id,  msg.as_string())
mail.close()

print('Message Delivered successfully!')