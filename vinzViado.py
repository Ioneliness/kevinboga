import os
import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from PIL import Image, ImageFont, ImageDraw
import time
from random import randint

frases = ['vinz deu o boga', 'kevin sama', 'eu dou o furebis', 'kevin, tenha um bom dia', 'eu te amo', 'voce me ama?', 'eu nao te xingo tanto', 'sera se voce ta bem', 'oi, tudo bem doutor?', 'eu amo memes', 'vinz ta dormindo', 'viado', 'oi tudo bem']

def SendMail():
    with open('image.jpg', 'rb') as f:
        img_data = f.read()
    msg = MIMEMultipart()
    msg['Subject'] = 'subject'
    msg['From'] = 'sorteionst@gmail.com'
    msg['To'] = 'burexcalibur@gmail.com'

    text = MIMEText("slc ...vinz e noga no comando papis")
    msg.attach(text)
    image = MIMEImage(img_data)
    msg.attach(image)

    print('cheguei0')
    login = 'sorteionst@gmail.com'
    password = 'Mari.1981'
    print('chegueiiii')
    context=ssl.create_default_context()
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.starttls(context=context)
    print('cheguei1')
    server.login(login, password)
    print('cheguei2')
    server.sendmail(
        'sorteionst@gmail.com', 'burexcalibur@gmail.com', msg.as_string()
    )    
    print('Sent')

def DesenharNoKevin():
    im = Image.open('kevin.jpg')
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype("Roboto-Regular.ttf", 40)
    minimal = 0
    maximun = len(frases) - 1
    draw.text((45, 250), frases[randint(minimal, maximun)], font=font)
    im.save('image.jpg')
    SendMail()
    
if __name__== "__vinzViado":
    while True:
        DesenharNoKevin()   
        time.sleep(360)
