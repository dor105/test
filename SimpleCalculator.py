from tkinter import *

root = Tk()
root.title("מחשבון")

e = Entry(root, width=35, borderwidth=4)
e.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

def button():
    return

#numbers

button_1 = Button(root,text="1",padx=35,pady=15,command=button) 
button_2 = Button(root,text="2",padx=35,pady=15,command=button) 
button_3 = Button(root,text="3",padx=35,pady=15,command=button) 
button_4 = Button(root,text="4",padx=35,pady=15,command=button) 
button_5 = Button(root,text="5",padx=35,pady=15,command=button) 
button_6 = Button(root,text="6",padx=35,pady=15,command=button) 
button_7 = Button(root,text="7",padx=35,pady=15,command=button) 
button_8 = Button(root,text="8",padx=35,pady=15,command=button) 
button_9 = Button(root,text="9",padx=35,pady=15,command=button) 
button_0 = Button(root,text="0",padx=35,pady=15,command=button) 



#function

button_plus = Button(root,text="+",padx=35,pady=15,command=button) 
button_equal = Button(root,text="=",padx=35,pady=15,command=button)
button_multi = Button(root,text="x",padx=35,pady=15,command=button) 
button_clear = Button(root,text="C",padx=35,pady=15,command=button) 
button_point = Button(root,text=".",padx=35,pady=15,command=button) 





#numbers

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)



#function
button_plus.grid(row=5, column=1)
button_equal.grid(row=5, column=2)
button_multi.grid(row=5, column=0)
button_clear.grid(row=4, column=2)
button_point.grid(row=4, column=1)




root.mainloop()
