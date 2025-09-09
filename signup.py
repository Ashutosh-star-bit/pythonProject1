from tkinter import *
import tkinter as tk
import fileinput
from tkinter import messagebox
import ast
import os
import pymysql
from PIL import ImageTk,Image
import customtkinter
import smtplib
import random
import turtle

def clear():
    emailEntry.delete(0,END)
    usernameEntry.delete(0,END)
    passwordEntry.delete(0,END)
    confirmEntry.delete(0,END)
    check.set(0)

def connect_database():
    if emailEntry.get()=='' or passwordEntry.get()=='' or usernameEntry.get()=='' or confirmEntry.get()=='':
        messagebox.showerror('Error','All Field Are Required')
    elif passwordEntry.get() != confirmEntry.get():
        messagebox.showerror('Error','Both Password Should Be Match')
    elif check.get()==0:
        messagebox.showerror('Error','Please accept Terms & Conditions')
    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='tiger')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Database Connectivity Issue, Please Try Again')
            return

        try:
            query = 'create database userdata'
            mycursor.execute(query)
            query= 'use userdata'
            mycursor.execute(query)
            query='create table data(id int auto_increment primary key not null,email varchar(50),username varchar(100),password varchar(20))'
            mycursor.execute(query)
        except:
            mycursor.execute('use userdata')
        query = 'select * from data where username=%s and email=%s'
        mycursor.execute(query,(usernameEntry.get(),emailEntry.get()))

        row = mycursor.fetchone()
        if row != None:
            messagebox.showerror('Error','Username Already exists')
        else:
            query = 'insert into data(email,username,password) value(%s,%s,%s)'
            mycursor.execute(query,(emailEntry.get(),usernameEntry.get(),passwordEntry.get()))
            con.commit()
            con.close()
            messagebox.showinfo('Success','Registration is successful')
            clear()
            signup_window.destroy()
            os.system('signin.py')



def login_page():
    signup_window.destroy()
    os.system('signin.py')


signup_window = Tk()

signup_window.state('zoomed')
signup_window.title('BUS RESERVATION SYSTEM')
signup_window.configure(bg="skyblue")
signup_window.resizable(False,False)

bgImage = ImageTk.PhotoImage(file = 'bg.jpg')

bgLabel = Label(signup_window ,image=bgImage)
bgLabel.place(x=250,y=80)

frame = Frame(signup_window,bg='white')
frame.place(x=804,y=181)

heading=Label(frame,text='CREATE AN ACCOUNT',font=('Microsoft Yahei UI Light',18,'bold'),bg='white',fg='firebrick1')
heading.grid(row=0,column=0,padx=10,pady=10)

emailLabel = Label(frame,text='Email',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
emailLabel.grid(row=1,column=0,sticky='w',padx=25,pady=(10,0))

emailEntry = Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),
                   fg='white',bg='firebrick1')
emailEntry.grid(row=2,column=0,sticky='w',padx=25)

usernameLabel = Label(frame,text='Username',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
usernameLabel.grid(row=3,column=0,sticky='w',padx=25,pady=(10,0))

usernameEntry = Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),
                   fg='white',bg='firebrick1')
usernameEntry.grid(row=4,column=0,sticky='w',padx=25)

passwordLabel = Label(frame,text='Password',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
passwordLabel.grid(row=5,column=0,sticky='w',padx=25,pady=(10,0))

passwordEntry = Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),
                   fg='white',bg='firebrick1')
passwordEntry.grid(row=6,column=0,sticky='w',padx=25)

confirmLabel = Label(frame,text='Confirm Password',font=('Microsoft Yahei UI Light',10,'bold'),bg='white',fg='firebrick1')
confirmLabel.grid(row=7,column=0,sticky='w',padx=25,pady=(10,0))

confirmEntry = Entry(frame,width=30,font=('Microsoft Yahei UI Light',10,'bold'),
                   fg='white',bg='firebrick1')
confirmEntry.grid(row=8,column=0,sticky='w',padx=25)

check = IntVar()
termsandconditions=Checkbutton(frame,text='I agree to the Terms & Conditions',font=('Microsoft Yahei UI Light',10,'bold'),
                               fg='firebrick1',bg='white',activebackground='white',activeforeground='firebrick1',
                               cursor='hand2',variable=check)
termsandconditions.grid(row=9,column=0,pady=10,padx=15)

signupButton = Button(frame,text='Signup',font=('Open Sans',16,'bold'),border=0,bg='firebrick1',fg='white',
                      activebackground='firebrick1',activeforeground='white',width=17,command=connect_database)
signupButton.grid(row=10,column=0,pady=10)

alreadyaccount = Label(frame,text='Already have an account',font=('Open Sans',9,'bold'),bg='white',fg='firebrick1')
alreadyaccount.grid(row=11,column=0,sticky='w',padx=25,pady=10)

loginButton = Button(frame,text='Log in',font=('Open Sans',9,'bold underline'),
                     bg='white',fg='blue',border=0,cursor='hand2',activebackground='white',
                     activeforeground='blue' ,command=login_page)
loginButton.place(x=175,y=405)


signup_window.mainloop()