import os
import smtplib
from email.message import EmailMessage

eaddress = os.environ.get('EMAIL_USER')
epassword = os.environ.get('EMAIL_PASS')

msg = EmailMessage()
msg['Subject'] = 'Email from Python'
msg['From'] = 'bala08mur@gmail.com'
msg['To'] = ['bala.rmur@gmail.com', 'shesiva@gmail.com']
txt = '''
import os
import smtplib
from email.message import EmailMessage

eaddress = os.environ.get('EMAIL_USER')
epassword = os.environ.get('EMAIL_PASS')

msg = EmailMessage()
msg['Subject'] = 'Email from Python'
msg['From'] = 'bala08mur@gmail.com'
msg['To'] = 'bala.rmur@gmail.com'
msg.set_content('This is a plain text email')

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(eaddress, epassword)
server.send_message(msg)
server.quit()
'''
msg.set_content(txt)

server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.login(eaddress, epassword)
server.send_message(msg)
server.quit()
