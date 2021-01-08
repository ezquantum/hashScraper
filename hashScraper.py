import requests, smtplib, hashlib
from email.message import EmailMessage
from urllib.request import urlopen

toAddress=['email@gmail.com', 'email@gmail.com', 'email@gmail.com']

url = 'https://www.heb.com/pharmacy/common/landing'
response = urlopen(url).read()
Hash1 = hashlib.sha224(response).hexdigest()

while True:

    try:

        response = urlopen(url).read()
        Hash1 = hashlib.sha224(response).hexdigest()
        time.sleep(10)
        response = urlopen(url).read()
        Hash2 = hashlib.sha224(response).hexdigest()

        if Hash2 == Hash1:
            continue

        else:

            message = EmailMessage()
            message.set_content(url)
            message['From'] = 'email@gmail.com'
            message['To'] = toAddress
            message['Subject'] = 'HEB News Page Has Updated. Check here https://www.heb.com/pharmacy/common/landing and https://newsroom.heb.com/covid-19-vaccine/'
            fromaddress = 'email@gmail.com'
            toaddress = toAddress
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
            server.login('email@gmail.com', 'password')
            server.send_message(message)
            server.quit()
            response = urlopen(url).read()
            Hash1 = hashlib.sha224(response).hexdigest()
            time.sleep(10)
            continue

    except Exception as e:

        message = EmailMessage()
        message.set_content(url)
        message['From'] = 'email@gmail.com'
        message['To'] = 'email@gmail.com'
        message['Subject'] = 'network implosion'
        fromaddress = 'email@gmail.com'
        toaddress = ['email@gmail.com']
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login('email@gmail.com', 'password')
        server.send_message(message)
        server.quit()
