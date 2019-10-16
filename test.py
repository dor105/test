'''
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
'''



'''
#2 version

import sys
print("Python version")
print (sys.version)
print("Version info.")
print (sys.version_info)
'''

'''
#3 Date & Time

import datetime     
now = datetime.datetime.now()
print ("Date & Time Now :")
print (now.strftime("%Y-%m-%d %H:%M:%S"))
'''


'''
#5 Reverse name

a=raw_input("Input your First Name :  b=raw_input("Input your L      ast Name : ")
print ("Hello  " + b + " " +      a)
    '''    

'''    
import getpass
import time 
import sys

counter = 0

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)

while (counter < 1 ):

    name = input("Insert a User Name :")
    if name == "dor_l" or name == "linoy_l": 
         password = getpass.getpass()
         if name == "dor_l" and password == "201135852":
             choice = input("---> welcome Dor levi ! <---\n\t Press the number from Option's:\n\t 1.Log off\n\t 2.Sleep\n\t 3.Shutdown\n\t")
             if choice == "1":
                 delay_print("------->log off from the system!")
                 print("\n")
             if choice == "2":
                 delay_print("-------> Go sleep!")
                 break
             if choice =="3":
                 delay_print("----------> Shuting down!")
                 break
     

         if name == "linoy_l" and password == "203266093" :
             choice = input("---> welcome Linoy levi ! <---\n\t Press the number from Option's:\n\t 1.Log off\n\t 2.Sleep\n\t 3.Shutdown\n\t")
             if choice == "1":
                 delay_print("------->log off from the system!")
                 print("\n")
             if choice == "2":
                 delay_print("-------> Go sleep!")
                 break
             if choice =="3":
                 delay_print("----------> Shuting down!")
                 break
         
        
'''

'''      
import os

def bla(file):
    if os.access(file,os.W_OK) is False:
        os.chmod(file,0o755)
    else:
        print("it's fine")


bla('/tmp') 
'''



