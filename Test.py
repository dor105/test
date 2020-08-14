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

'''
#return true if That's exactly same number in da range
def test_distinct(data):
  if len(data) == len(set(data)):
    return True
  else:
    return False;
print(test_distinct([1,5,5,9]))
'''

'''
#json libary
import json

with open ('test.json') as json_data:
    data = json.load(json_data)
    for i in data['Os']:
        print i['Name']+i['Version']+ " " +i['Kernel']
 
'''


class clubsisr:

    # class attribute
    st1 = "1st Place"
    st2 = "8st Place"

    # instance attribute
    def __init__(self, name, champion):
        self.name = name
        self.champion = champion

# instantiate the clubs class
yelo = clubsisr("FCBJ", 8)
red = clubsisr("FCHT", 5)

# access the class attributes
print("Beitar Jeruslem is a {}".format(yelo.__class__.st1))
print("Hapoel Tel-aviv is a {}".format(red.__class__.st2))

# access the instance attributes
print("{} is a {} championship's in israel leage".format( yelo.name, yelo.champion))
print("{} is a {} championship's in israel leage".format( red.name, red.champion))

#That