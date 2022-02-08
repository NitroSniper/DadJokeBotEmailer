import requests
import json

APISite = 'https://icanhazdadjoke.com/'
userAgent = 'Mozilla/5.0'

headers = {
    'Accept': 'text/plain',
    'User-Agent': 'My Libary (https://github.com/NitroSniper/DadJokeAndEmailer)'
}   
response = requests.get(headers=headers, url=APISite)
dadJoke = response.content.decode('utf-8')


senderEmail = '' #Enter the email of the sender you are gonna use. make sure it is gmail
receiverEmails = [] #enter the name of the recipient in a string.


message = '''\
Subject:DadJoke
%s

By Ortin Fargo >:D

- NoMercy 
''' % dadJoke

import smtplib, ssl

port = 465  # For SSL
password = #NOTHING TO SEE HERE LDSAJFLASDJFLJSLDFKLSDFJKL

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(senderEmail, password)
    for receiverEmail in receiverEmails:
        server.sendmail(senderEmail, receiverEmail, message)