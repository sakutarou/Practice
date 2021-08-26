# -*- coding: utf-8 -*-
import email.message
msg = email.message.EmailMessage()
msg["From"] = "master.am03@g2.nctu.edu.tw"
msg["To"] = "master.am03@g2.nctu.edu.tw"
msg["Subject"] = "安安"
#msg.set_content("安安你好")
msg.add_alternative("<h3>哈囉你好</h3>",subtype = "html")
import smtplib
server = smtplib.SMTP_SSL("smtp.gmail.com",465)
server.login("k31415926ast@gmail.com","oijpsjplicagoety")
server.send_message(msg)
server.close()

