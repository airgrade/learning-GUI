from tkinter import *

def add():
    '''functon to add the two numbers in the input widgets'''
    
    #picking the numbers put in from the users
    n1 = int(number1.get())
    n2 = int(number2.get())
    
    result = str((n1 + n2))
    answer.config(text="Answer is: " + result)

root = Tk()

#screen size
root.geometry("300x300")

#input box for user
number1 = Entry(root)
number2 = Entry(root)
number1.pack()
number2.pack()

button = Button(root,text='add',command=add)
button.pack()

answer = Label(root)
answer.pack()


root.mainloop()