#for i in range(1,11):
#   print(i) 



#Mylist = ["Dor","Linoy","Ronit", "Amnon"]
#for name in Mylist:
#    print ("My name is:" + name) 


"""
name = input("Enter your name : ")

if name == "dor":
    print ("Welcome to Web server" )
else:
 print ("accsess denied!")
 """
 

from string import Template

def  Main():
    cart = []
    cart.append(dict(item="Totit", price=3 ,qty=3))
    cart.append(dict(item="Beer", price=6 ,qty=2))          
    cart.append(dict(item="Cake", price=8,qty=1))          

    t = Template("$qty x $item = $price Usd")
    total = 0
    print("Receipt")
    for data in cart:
            print(t.substitute(data))
            total+= data["price"]*data["qty"]
    print("Total: "+str(total)+"$")

#if __name__ == '_main_':
Main()


