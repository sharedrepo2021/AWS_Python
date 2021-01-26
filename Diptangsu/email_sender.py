import smtplib

server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
server.login('from', 'password')
server.sendmail('from', 'to', 'message')
server.quit()