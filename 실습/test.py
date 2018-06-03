<<<<<<< HEAD
#-*- coding: utf-8 -*-
import smtplib

s = smtplib.SMTP('smtp.gmail.com', 587)
s.ehlo()

s.starttls()
s.ehlo()
s.login("xoghk9zla@gmail.com", "d7297mc!")
=======
from tkinter import *
window = Tk()
button = Button(window, text="클릭!")
button.pack()
window.mainloop()
>>>>>>> 7466e675c8a35d7e9abb866b1edef1b1102cb7ec
