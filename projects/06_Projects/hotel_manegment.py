"""
Use:
while loop
functions (tons)
use returns
dictionary
tuples
lists

Create:
A check in and check out system
Something new

Tax= in total 1.0775
"""

from guizero import App, Box, Text, TextBox, PushButton, ListBox, error
from tkinter import messagebox, simpledialog, Tk

def pay_with_cash(one,five,ten,twenty,fifty,hundred):
    paid=0
    one = simpledialog.askinteger("Cash","How many one dollor bills do you want to use?")
    paid=paid+1
    five = simpledialog.askinteger("Cash","How many five dollor bills do you want to use?")
    
def pay():
    way_to_pay=simpledialog.askstring("","Cash or card?")
    if way_to_pay=="card":
        credit_num=simpledialog. askinteger("Almost done!","Enter your credit card number.")
    else:
        if way_to_pay=="cash":
            
        else:
             messagebox.showinfo(message="I'll assume cash" )       
        

def check_in(rooms,price):
    name=simpledialog.askstring
    return rooms*price
    messagebox.showinfo(message="thank you for your purchase, have a nice time!" )

running=True
while running:
    ask=simpledialog.askstring("","Would you like to continue" )
    if ask=="no":
        running = False