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
rooms = {}
room_num = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
total_price = 0
rooms_borrowing=0
ratings=[]
nums=0
def rate():
    rate=simpledialog.askinteger("Rate this hotel","Rate this hotel from 1 to 5")
    if rate> 0 and rate<6:
            ratings.append(rate)
    else:
        simpledialog("","That is two big or too small" )
        rate()
def pay_with_cash(amount_paying):
    if amount_paying == total_price:
        messagebox.showinfo(message="Great!")
    else:
        if amount_paying > total_price:
            messagebox.showinfo(message="Here is your " +
                                str(amount_paying-total_price)+" cash back")

        else:
            messagebox.showinfo(
                message="you need"+str(total_price-amount_paying) + " more dollars")
            messagebox.showinfo("", "5 minutes later...")
            messagebox.showinfo("","Thank you for your purchase")


def pay():
    way_to_pay = simpledialog.askstring("", "Cash or card?")
    if way_to_pay == "card":
        credit_num = simpledialog. askinteger(
            "Almost done!", "Enter your credit card number.")
        messagebox.showinfo("","loading..")
    else:
        if way_to_pay == "cash":
            amount = simpledialog.askinteger("Pay", "How many dollars?")
            pay_with_cash(amount)
        else:
            messagebox.showinfo(message="I'll assume cash")
            simpledialog.askinteger("Pay", "How many dollars?")
            pay_with_cash(amount)


def check_in():
    name = simpledialog.askstring("Name", "What's your name?")
    pay()
    for a in range(rooms_borrowing):    
        rooms[len(rooms)] = name
        messagebox.showinfo(
        message="thank you for your purchase, have a nice time!")

def check_out():
    del_room= simpledialog.askinteger("","What room number are you?")
    if del_room in rooms:
        del_name=simpledialog.askstring("","What is your name?")
        if rooms[del_room]==del_name:
            del rooms[del_room]
            messagebox.showinfo("","Hope you had a nice time, thank you!")
        else:
            messagebox.showinfo("","Wrong name, try again")
            

    else:
        messagebox.showinfo("","That room is empty, try again" )
        check_out
running = True
while running:
    in_or_out = simpledialog.askstring("Hello", "are you checking in or out?")
    if in_or_out == "in":
        if len(rooms) > 9:
            messagebox.showinfo("","Sorry we are full")
        else:
            rooms_borrowing = simpledialog.askinteger(
                "", "How many rooms are you going to use?")
            if rooms_borrowing+len(rooms) > 10:
                messagebox.showinfo("", "too many rooms!")
            else:
                nights=simpledialog.askinteger("","How many nights?")
                total_price = rooms_borrowing*nights*100*1.08
                messagebox.showinfo("", "It is " + str(total_price)+" dollars")
                check_in()
    if in_or_out== "out":
        check_out()
        rate()
        nums=0
        for num in ratings:
            nums+=num
        messagebox.showinfo("","This hotel has "+str(nums/len(ratings))+" stars")

    messagebox.showinfo("The rooms", rooms)
    ask = simpledialog.askstring("", "Would you like to continue?")
    if ask == "no":
        running = False
