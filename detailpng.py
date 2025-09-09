import tkinter as tk
from tkinter import *
import customtkinter
from tkinter import messagebox
import json
from tkcalendar import DateEntry
from PIL import ImageTk,Image
import os
import pymysql
import threading
import time
import mysql.connector

with open('user_input.json', 'r') as f:
    user_details = json.load(f)

def clear():
    name.delete(0,END)
    age.delete(0,END)
    gender.delete(0,END)

def connect_database():
    if name.get()=='' or age.get()=='' or gender.get()=='' :
        messagebox.showerror('Error','All Field Are Required')
    elif name.get()=='':
        messagebox.showerror('Error','Name Is Required')
    elif gender.get()=='':
        messagebox.showerror('Error','Gender Is Required')
    elif age.get()=='':
        messagebox.showerror('Error','Age Is Required')
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
        query = 'select * from passenger where journey_date=%s and passenger_name=%s'
        mycursor.execute(query,(date_entry.get(),name.get()))

        row = mycursor.fetchone()
        if row != None:
            messagebox.showerror('Error','Passenger Already exists')
        else:
            data = [name.get(), gender.get(),age.get(),date_entry.get(),variable.get(),str(user_details[0]),str(user_details[1])]

            # Write data to a JSON file
            with open('passenger_detail.json', 'w') as f:
                json.dump(list(data), f)

            win.destroy()
            os.system('paymentpng.py')
        con.commit()
        con.close()

def open_file():
    win.destroy()
    os.system('q.py')


win = tk.Tk()
win.title("ticket page")
win.state("zoomed")
win.configure(bg="#fff")
win.resizable(False,False)
main_frame = tk.Frame(win , bg="black" , pady=40)
main_frame.pack(fill=tk.BOTH ,expand=True)

img9 = ImageTk.PhotoImage(Image.open("border1.png").resize((1380,700)))

border = Label(main_frame, image=img9, border=0, bg='black')
border.place(x=85,y=0)

l1 = tk.Label(main_frame , text="Please Enter Passenger Details",font=('Arial',24,'bold'),
                          bg='black',fg='#E1FF33')
l1.place(x=535,y=80)

label1 = Label(main_frame,text='Passenger Name',font=('Arial',18,'bold'),
                      bg='black',fg='#FFE555')
label1.place(x=340,y=180)

name = Entry(main_frame,width=25,fg='#ECFF67',font=('Arial',16,'bold'),
                       border=1,bg='black')
name.place(x=340,y=215)

label2 = Label(main_frame,text='Gender',font=('Arial',18,'bold'),
                      bg='black',fg='#FFE555')
label2.place(x=750,y=180)

gender = Entry(main_frame,width=15,fg='#ECFF67',font=('Arial',16,'bold'),
                       border=1,bg='black')
gender.place(x=750,y=215)

label3 = Label(main_frame,text='Age',font=('Arial',18,'bold'),
                      bg='black',fg='#FFE555')
label3.place(x=1050,y=180)

age = Entry(main_frame,width=8,fg='#ECFF67',font=('Arial',16,'bold'),
                       border=1,bg='black')
age.place(x=1050,y=215)

label4 = Label(main_frame,text='Date of Journey',font=('Arial',18,'bold'),
                      bg='black',fg='#FFE555')
label4.place(x=540,y=300)

date_entry = DateEntry(main_frame, date_pattern='yyyy-mm-dd',border=0,font=('Arial',15,'bold'))
date_entry.place(x=540,y=340)
date_entry.config(background='black',foreground='#ECFF67')

img1= ImageTk.PhotoImage(Image.open("backbutton.png").resize((50,50)))

button8 = tk.Button(master=main_frame ,image=img1 ,border=0,borderwidth=0,bg='black',activebackground='black', cursor = 'hand2',command=open_file)
button8.place(x=250 , y= 80)

label5 = Label(main_frame,text='Bus type',font=('Arial',18,'bold'),
                      bg='black',fg='#FFE555')
label5.place(x=835,y=300)
variable = tk.StringVar()
variable.set('AC')

list_option = ['AC','Non AC','Seater','Sleeper']
select_option = tk.OptionMenu(
    main_frame,variable,*list_option
)

select_option.config(
    bg='black',fg='#ECFF67',activebackground='black',font=('Arial',16),
    highlightbackground='black',indicatoron=0,cursor='hand2',width=15,height=0,borderwidth=1,
)

select_option.grid(column = 835 , row=335,sticky=tk.N+tk.EW ,padx =835,pady = (335,0))

submitbutton = customtkinter.CTkButton(master=main_frame,text="Submit" ,width=100 ,height=20 ,text_color='red',
                                       hover_color='#1A98FF', font=('Arial',30, 'bold'),corner_radius=50,
                                       cursor = 'hand2',command=connect_database)
submitbutton.place(x=700,y=460)

win.mainloop()