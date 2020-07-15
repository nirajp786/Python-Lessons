from tkinter import *

def convert_kg():
    # Get user value from input box and multiply by 1000 to get kilograms
    gram = float(e1Value.get())*1000
    pound = float(e1Value.get())*2.20462
    ounce = float(e1Value.get())*35.274
    
    # Empty the Text boxes if they had text from the previous use and fill them again
    t1.delete("1.0", END)  # Deletes the content of the Text box from start to END
    t1.insert(END,gram)  # Fill in the text box with the value of gram variable
    t2.delete("1.0", END)
    t2.insert(END,pound)
    t3.delete("1.0", END)
    t3.insert(END,ounce)

root = Tk()

# Create a Label widget with "Kg" as label
l1 = Label(root, text="Kg")
l1.grid(row=0, column=0)  # The Label is placed in position 0, 0 in the window

#Create a StringVar object to store stuff written in entry 
e1Value = StringVar()
e1 = Entry(root, textvariable=e1Value)
e1.grid(row=0, column=1)

#Create a button
b1 = Button(root, text="Convert", command=convert_kg)
b1.grid(row=0, column=2)

# Create three empty text boxes, t1, t2, and t3
t1=Text(root,height=1,width=20)
t1.grid(row=1,column=0)
 
t2=Text(root,height=1,width=20)
t2.grid(row=1,column=1)
 
t3=Text(root,height=1,width=20)
t3.grid(row=1,column=2)

root.mainloop()