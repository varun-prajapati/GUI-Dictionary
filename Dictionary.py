from tkinter import *

import json
from difflib import get_close_matches

# Function Definitions
def nearmatch(user_data, keys):
    return get_close_matches(user_data,keys)


def printer_func(data, items):
    t1.delete(1.0, END)
    for value in items:
        t1.insert(END, value + '\n')

def data_check(user_data, keys, data1):
    if user_data in keys:
        item1 = data1[user_data]
        printer_func(user_data, item1)
        return 1
    elif user_data.title() in keys:
        item1 = data1[user_data.title()]
        printer_func(user_data.title(), item1)
        return 1
    elif user_data.upper() in keys:
        item1 = data1[user_data.upper()]
        printer_func(user_data.upper(), item1)
        return 1
    elif user_data.lower() in keys:
        item1 = data1[user_data.lower()]
        printer_func(user_data.lower(), item1)
        return 1
    else:
        return 0

def get_dict_value(user_data, keys, data1):
    if data_check(user_data,keys,data1):
            user_data = "/exit"
    else:
        closematch = nearmatch(user_data,keys)
        if len(closematch) > 0:
            t1.delete(1.0, END)
            t1.insert(END, "Did you mean one of these:"  + '\n')
            for value in closematch:
                t1.insert(END, value + '\n')
        else:
            t1.delete(1.0, END)
            t1.insert(END, "Word does not exist in language" + '\n')



def get_val_from_Screen():
    data1 = json.load(open("data.json"))
    keys = data1.keys()
    get_dict_value(user_value.get(),keys, data1)




# Main Function
window = Tk()

b1 = Button(window, text = "Get Definition", command=get_val_from_Screen)
b1.grid(row=2, column=1,columnspan = 2)
e2 = Label(window, text="Enter the word:")
e2.grid(row = 0, column=0)
user_value = StringVar()
e1 = Entry(window,textvariable=user_value)
e1.grid(row = 0, column=3)
t12 = Label(window, text=" Definition(s):")
t12.grid(row = 3, column=0)
t1=Text(window, height=30, width=80)
t1.grid(row = 4, column = 0, columnspan = 4)


window.mainloop()
