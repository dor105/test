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


"""
'''
#fibonache
a, b = 0, 1
while b < 100:
    print(b)
    a, b = b, a + b
'''

'''
#def example
def ex_fun(x):
    return x+1

ex_var = 10
print(ex_var)

processed_var = ex_fun(ex_var)
print(processed_var)
'''


'''
def complicated(x,y):

    def squared(a): #def inside def
        return a*a

    x_squared = squared(y)
    return x_squared + y * 5


x = 5
y = 3

print(complicated(x,y))
'''

def test_distinct(data):
  if len(data) == len(set(data)):
    return True
  else:
    return False;
print(test_distinct([1,5,5,9]))







