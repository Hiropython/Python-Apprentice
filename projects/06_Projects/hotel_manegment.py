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
rooms={}
room_num=(1,2,3,4,5,6,7,8,9,10)
total_price=0
def pay_with_cash(amount_paying):
    if amount_paying==total_price:
        messagebox.showinfo(message="Great!")
    else:
        if amount_paying>total_price:
            messagebox.showinfo(message="Here is your "+amount_paying-total_price+" cash back")
            
        else:
            messagebox.showinfo(message="you need"+total_price-amount_paying+ "more money")
            messagebox.showinfo(message="Thank you for your purchase")
def pay():
    way_to_pay=simpledialog.askstring("","Cash or card?")
    if way_to_pay=="card":
        credit_num=simpledialog. askinteger("Almost done!","Enter your credit card number.")
    else:
        if way_to_pay=="cash":
            amount=simpledialog.askinteger("Pay","How many dollars?")
            pay_with_cash(amount)
        else:
            messagebox.showinfo(message="I'll assume cash" )       
            simpledialog.askinteger("Pay","How many dollars?")
            pay_with_cash(amount)

def check_in(price):
    name=simpledialog.askstring("Name","What's your name?")
    
    for i in range (len(room_num)):
        if i not in rooms.values():
            
            rooms[name]=i
            break

    
    messagebox.showinfo(message="thank you for your purchase, have a nice time!" )

running=True
while running:
    in_or_out=simpledialog.askstring("Hello","are you checking in or out?")
    if in_or_out=="in":
        if len(rooms)>10:
            messagebox.showinfo("Sorry we are full")
        else:
            rooms_borrowing=simpledialog.askinteger("","How many rooms are you going to use?")
            
            if rooms_borrowing+len(rooms)>10:
                messagebox.showinfo("to many rooms!")
            else:
                total_price=total_price=rooms*price*1.08
                messagebox.showinfo("It is"+ total_price+"dollars")
                for j in range(rooms_borrowing):
                    check_in(100)
    ask=simpledialog.askstring("","Would you like to continue?" )
    if ask=="no":
        running = False

           