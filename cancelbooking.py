import tkinter as tk
from tkinter import *
import customtkinter
from tkinter import messagebox
import json
import re
from datetime import date
from tkcalendar import DateEntry
from PIL import ImageTk,Image
import os
import pymysql
def back():
    root.destroy()
    os.system('q.py')
def connect_database():
    if name.get()=='' or e1.get()=='Leaving from' or e2.get()=='Going to':
        messagebox.showerror('Error','All Field are Required')
    else:
        try:
            con = pymysql.connect(host='localhost', user='root', password='tiger')
            mycursor = con.cursor()
        except:
            messagebox.showerror('Error', 'Database Connectivity Issue, Please Try Again')
            return

        try:
            query = 'use userdata'
            mycursor.execute(query)
            query = 'create table passenger(id int auto_increment primary key not null,passenger_name varchar(100),gender varchar(10),age int,journey_date date,bus_type varchar(50),leaving_from varchar(50),going_to varchar(50),payment(50) NOT NULL DEFAULT "Successful")'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata')
        query = 'select * from passenger where journey_date=%s and passenger_name=%s and leaving_from=%s and going_to=%s'
        mycursor.execute(query, (date_entry.get(), name.get(),e1.get(),e2.get()))
        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror('Error', 'Invalid Passenger Details')
        else:
            mycursor.execute('use userdata')
            query = 'delete from passenger where (journey_date=%s) and (passenger_name=%s) and (leaving_from=%s) and (going_to=%s)'
            mycursor.execute(query, (date_entry.get(), name.get(), e1.get(), e2.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success','Booking Cancel Successfully')



root = tk.Tk()
# root.title('Home Page')
root.state('zoomed')
root.configure(bg="#fff")
root.resizable(False,False)

main_frame = tk.Frame(root , bg="black" , pady=40)
main_frame.pack(fill=tk.BOTH ,expand=True)

img = ImageTk.PhotoImage(Image.open("border7.png").resize((1380,800)))

border = Label(main_frame, image=img, border=0, bg='black')
border.place(x=85,y=-15)

heading = Label(main_frame,text='Cancel Booking' ,fg='#1EFFC3' ,bg="black", font=('Arial',35,'bold'))
heading.place(x=640,y=110)

label1 = Label(main_frame,text='Passenger Name',font=('Arial',18,'bold'),
                      bg='black',fg='#FFE555')
label1.place(x=440,y=230)

name = Entry(main_frame,width=25,fg='#ECFF67',font=('Arial',16,'bold'),
                       border=1,bg='black')
name.place(x=445,y=265)

label4 = Label(main_frame,text='Date of Journey',font=('Arial',18,'bold'),
                      bg='black',fg='#FFE555')
label4.place(x=850,y=230)

date_entry = DateEntry(main_frame, date_pattern='yyyy-mm-dd',border=0,font=('Arial',15,'bold'))
date_entry.place(x=855,y=265)
date_entry.config(background='black',foreground='#ECFF67')

submitbutton = customtkinter.CTkButton(master=main_frame,text="Submit" ,width=100 ,height=20 ,text_color='red',
                                       hover_color='#1A98FF', font=('Arial',30, 'bold'),corner_radius=50,
                                       cursor = 'hand2',command=connect_database)
submitbutton.place(x=700,y=460)

font1 = ('Times',18,'italic')
my_list = ['Mirzapur' ,'Prayagraj' ,'Kanpur','Vanarasi','Lucknow','Bareilly']
def my_upd1(my_widget):
    main_frame = my_widget.widget
    index = int(main_frame.curselection()[0])
    value = main_frame.get(index)
    e1_str.set(value)
    l1.delete(0,END)
def my_down1(my_widget):
    l1.focus()
    l1.selection_set(0)
def my_upd2(my_widget):
    main_frame = my_widget.widget
    index = int(main_frame.curselection()[0])
    value = main_frame.get(index)
    e2_str.set(value)
    l2.delete(0,END)
def my_down2(my_widget):
    l2.focus()
    l2.selection_set(0)
def on_enter(e):
    e1.delete(0,'end')
def on_leave(e):
    if e1.get()=='':
        e1.insert(0,'Leaving from')

e1_str = tk.StringVar()
e1 = tk.Entry(main_frame,font=font1,textvariable=e1_str,fg='#1A98FF' )
e1.place(x=440,y=340)
e1.insert(0,'Leaving from')
e1.bind('<FocusIn>' , on_enter)
e1.bind('<FocusOut>',on_leave)
l1 = tk.Listbox(main_frame,height=4,width=15,font=font1,relief='solid' ,bg='black' ,fg="#1A98FF",border=0,highlightthickness=0)
l1.place(x=440,y=375)
def on_enter(e):
    e2.delete(0,'end')
def on_leave(e):
    if e2.get()=='':
        e2.insert(0,'Going to')

e2_str = tk.StringVar()
e2 = tk.Entry(main_frame,font=font1,textvariable=e2_str ,fg='#1A98FF')
e2.place(x=850,y=340)
e2.insert(0,'Going to')
e2.bind('<FocusIn>' , on_enter)
e2.bind('<FocusOut>',on_leave)
l2 = tk.Listbox(main_frame,height=4,width=15,font=font1,relief='flat' ,bg='black' ,highlightthickness=0 ,fg="#1A98FF",border=0)
l2.place(x=850,y=375)
def get_data1(*args):
    search_str = e1.get() # user entered string
    l1.delete(0,END)
    for element in my_list:
        if(re.match(search_str ,element,re.IGNORECASE)):
            l1.insert(tk.END,element)
def get_data2(*args):
    search_str = e2.get() # user entered string
    l2.delete(0,END)
    for element in my_list:
        if(re.match(search_str ,element,re.IGNORECASE)):
            l2.insert(tk.END,element)

# l1.bind("<<ListboxSelect>>",my_upd)
e1.bind('<Down>',my_down1)
l1.bind('<Return>',my_upd1)
l1.bind('<Right>',my_upd1)
e1_str.trace('w',get_data1)

e2.bind('<Down>',my_down2)
l2.bind('<Return>',my_upd2)
l2.bind('<Right>',my_upd2)
e2_str.trace('w',get_data2)

img2= ImageTk.PhotoImage(Image.open("backbutton.png").resize((50,50)))

button8 = tk.Button(master=main_frame ,image=img2 ,border=0,borderwidth=0,bg='black',activebackground='black', cursor = 'hand2',command=back)
button8.place(x=450 , y=120)

root.mainloop()