#-*- coding: utf-8 -*-
import smtplib

s = smtplib.SMTP('smtp.gmail.com', 587)
s.ehlo()

s.starttls()
s.ehlo()
s.login("xoghk9zla@gmail.com", "d7297mc!")
