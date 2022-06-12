from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector

mydb=mysql.connector.connect(host="localhost",username="root",password="",database="stationaryshop")
my_cur=mydb.cursor()

window=Tk()
window.title("Stationery Shop")
window.geometry("1000x700")
window.configure(bg='cyan')

def addproduct():

    e1 = entry1.get()
    e2 = entry2.get()
    e3 = entry3.get()
    e4 = entry4.get()
    try:
        if (e1 != "" and e2 != "" and e3 != "" and e4 != ""):
            if(e1.isdigit() == False ):
                my_cur.execute(f'INSERT INTO stationaryshopdb (product_name,product_price,product_quantity,product_discount) VALUES ("{e1.lower()}","{e2}","{e3}","{e4}")')
                mydb.commit()
                entry1.delete(0, END)
                entry2.delete(0, END)
                entry3.delete(0, END)
                entry4.delete(0, END)
                messagebox.showinfo("ADD ITEM", "ITEM ADDED SUCCESSFULLY....!!!")
            else:
                messagebox.showinfo("ERROR", "Item Name and Item Category can't be in Numbers")
        else:
            messagebox.showinfo("ERROR", "ENTER ALL DETAILS ...!!!")
    except ValueError:
        messagebox.showinfo("ERROR", "Item Price, quantity, discount can't be in String")

def showdatabase():
    my_cur.execute("SELECT * From stationaryshopdb")
    records=my_cur.fetchall()
    #print_record=''
    mytext = Text(window, width=90, height=20, bg="gray",
                  fg="black", font=("Times", 12))
    mytext.insert(
        END, " Product_Name \t\tProduct_Price \t\tProduct_Quantity \t\tProduct_Discount \n")
    mytext.insert(
        END, " ------------ \t\t----------- \t\t-------------- \t\t--------------- \n")
    for record in records:
         mytext.insert(END, "       {0} \t\t     {1} \t\t         {2} \t\t   {3}\n".format(
            record[0], record[1], record[2], record[3]))
    mytext.grid(row=7,column=0,columnspan=4)


def deleteproduct():
    e1 = entry1.get()
    if e1 != "SEARCH" and e1 != "":
            my_cur.execute(f"DELETE from stationaryshopdb WHERE product_name = '{e1.lower()}'")
            mydb.commit()
            messagebox.showinfo("DELETE ITEM", "ITEM DELETED SUCCESSFULLY....!!!")
    else:
        messagebox.showwarning("NO DATA", "PLEASE ENTER ANY NAME....!!!")

def searchproduct():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    e5 = entry5.get()
    if e5 == "":
        {
            messagebox.showwarning(
                "Warning", "Please first enter item name for search")
        }
    else:
        my_cur.execute(f"select * from stationaryshopdb where product_name = '{e5.lower()}'")
        mytext1 = my_cur.fetchone()
        if mytext1 == None and e5 !="":
            messagebox.showinfo("Error", "Element not exist")
        else:
            entry1.insert(0, mytext1[0])
            entry2.insert(0, mytext1[1])
            entry3.insert(0, mytext1[2])
            entry4.insert(0, mytext1[3])
            entry5.insert(0, mytext1[4])
def clear():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)

label0=Label(window, text="STATIONARY STORE MANAGEMENT SYSTEM ",width=40,font=(15))
label0.grid(row=0,column=0,columnspan=4,padx=5,pady=5)
label1=Label(window,text="Product Name",bg="blue", fg="white",font=(12),bd=8,
               relief="ridge", width=25)
label1.grid(row=2,column=0,padx=5,pady=5)
label2=Label(window,text="Price Of Product",bg="blue", fg="white",font=(12),bd=8,
               relief="ridge", width=25)
label2.grid(row=3,column=0,padx=5,pady=5)
label3=Label(window,text="Quantity Of Product",bg="blue", fg="white",font=(12),bd=8,
               relief="ridge", width=25)
label3.grid(row=4,column=0,padx=5,pady=5)
label4=Label(window,text="Discount On The Product",bg="blue", fg="white",font=(12),bd=8,
               relief="ridge", width=25)
label4.grid(row=5,column=0,padx=5,pady=5)


button1=Button(window,activebackground="green", text="Add Product",command=addproduct,bd=8,
                 width=25, font=("Times", 14))
button1.grid(row=6, column=0, padx=10, pady=10)
button1.bind('<Button-1>',addproduct)

button2=Button(window, activebackground="green", text="Delete Product", bd=8,
                 width=25, font=("Times", 14),command=deleteproduct)
button2.grid(row=6, column=1, padx=10, pady=10)
button2.bind('<Button-1>',deleteproduct)
button3=Button(window, activebackground="green", text="Show Database", bd=8,
                 width=25, font=("Times", 14),command=showdatabase)
button3.grid(row=4, column=3, padx=10, pady=10)
button3.bind('<Button-1>',showdatabase)
button4=Button(window, activebackground="green", text="SEARCH ITEM", bd=8,
                 width=25, font=("Times", 14),command=searchproduct)
button4.grid(row=3, column=3, padx=10, pady=10)
button3.bind('<Button-1>',searchproduct)

button4=Button(window, activebackground="green", text="Clear", bd=8,
                 width=25, font=("Times", 14),command=clear)
button4.grid(row=6, column=3, padx=10, pady=10)
button4.bind('<Button-1>',clear)

entry1=Entry(window,font=("Times", 14), bd=8, width=30, bg="white")
entry1.grid(row=2,column=1,padx=5,pady=5)
entry2=Entry(window,font=("Times", 14), bd=8, width=30, bg="white")
entry2.grid(row=3,column=1,padx=5,pady=5)
entry3=Entry(window,font=("Times", 14), bd=8, width=30, bg="white")
entry3.grid(row=4,column=1,padx=5,pady=5)
entry4=Entry(window,font=("Times", 14), bd=8, width=30, bg="white")
entry4.grid(row=5,column=1,padx=5,pady=5)
entry5=Entry(window,font=("Times", 14), bd=8, width=30, bg="white")
entry5.grid(row=2,column=3,padx=5,pady=5)

window.mainloop()