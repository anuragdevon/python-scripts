#!usr/bin/python3

# python program to send gamil from my account
import smtplib

# creating a SMTP session

session = smtplib.SMTP('smtp.outlook.com', 587)

# starting TLS for the security
session.starttls()

# Authentication
session.login("anuragkar@outlook.com", "andromeda@11")

# storing the message to be sent
message = "hwllo workd"

# sending the email
session.sendmail("anuragkar@outlook.com", "skkrttc@gmail.com", message)

# terminating the session
session.quit()










