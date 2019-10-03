"""
#Turtle Game!

import turtle

wn =turtle.Screen()
wn.bgcolor("white")

tina = turtle.Turtle()
tina.shape('turtle')

tina.left(90)
tina.forward(35)
tina.write("What color am I now?")

tina.forward(35)
tina.color("blue")
tina.write("What color am I now?")

tina.forward(35)
tina.color("purple")
tina.write("What color am I now?")

tina.forward(35)
tina.color("green")
tina.write("What color am I now?")

tina.left(90)
tina.forward(35)
tina.left(90)

delay = raw_input("press enter to finsih the game.")
"""



"""
#2 version

import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)
"""

"""
#3 Date & Time

import datetime     
now = datetime.datetime.now()
print ("Date & Time Now :")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
"""


"""
#5 Reverse name

a=raw_input("Input your First Name : ")
b=raw_input("Input your Last Name : ")
print ("Hello  " + b + " " + a)
"""


