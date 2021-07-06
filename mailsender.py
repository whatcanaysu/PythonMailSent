# -*- coding: utf-8 -*-
"""
Created on Thu Jun 17 15:11:48 2021

@author: aysu.demir
"""
adress = 'demo@gmail.com'
password = '1234'
msg = "this was sent using python!!"
import smtplib
server = smtplib.SMTP('smtp.gmail.com',587)
server.starttls()
server.login(adress, password)
print("login success")
server.sendmail(adress, 'to@gmail.com', msg)
print("sent!")

    