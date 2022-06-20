from tkinter import *
def displayValue():
    print("working")
    print(f"{userValue.get() , genderValue.get(),phnValue.get() ,ageValue.get() ,paymodeValue.get(),foodServiceValue.get()}")

    with open("record.txt",'a') as file:
        file.write(f"{userValue.get() , genderValue.get(),phnValue.get() ,ageValue.get() ,paymodeValue.get(),foodServiceValue.get() }\n",)

       
root = Tk()
root.geometry("500x500")
root.title("Travel Agency")

Label(root,text="Wheels on the Bus",foreground="red",font="bold 20",padx=20).grid(row=0,column=1)

name = Label(root,text="Name").grid(row=1)
gender = Label(root,text="Gender").grid(row=2)
phn = Label(root,text="Phn").grid(row=3)
age = Label(root,text="Age").grid(row=4)
paymode = Label(root,text="Payment Mode").grid(row=5)
food = Label(root,text="Food Service").grid(row=6)

#stringVar

userValue=StringVar()
genderValue=StringVar()
phnValue=IntVar()
ageValue=IntVar()
paymodeValue=StringVar()
foodServiceValue=IntVar()

#Entries Value
nameEntry = Entry(root,textvariable=userValue).grid(row=1,column=1)
genderEntry = Entry(root,textvariable=genderValue).grid(row=2,column=1)
phnEntry = Entry(root,textvariable=phnValue).grid(row=3,column=1)
ageEntry = Entry(root,textvariable=ageValue).grid(row=4,column=1)
paymodeEntry = Entry(root,textvariable=paymodeValue).grid(row=5,column=1)

#checkbox
foodentry = Checkbutton(text="Do you Need Meal",variable=foodServiceValue)
foodentry.grid(row=6,column=1)

Button(root,text="Submit",command=displayValue).grid(row = 7,column=1)


#foodEntry = Entry(root,textvariable=foodServiceValue).grid(row=6,column=1)

root.mainloop()
