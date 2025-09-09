from tkinter import *
import tkinter as tk
import fileinput
from tkinter import messagebox
import ast
import os
import pymysql
import json
from PIL import ImageTk,Image
import customtkinter
import smtplib
import random
import turtle

def forget_pass():
    def change_password():
        if user_entry.get()=='' or email_entry.get()=='' or newpass_entry.get()=='' or confirmpass_entry.get()=='':
            messagebox.showerror('Error','All Field Are Required',parent=window)
        elif newpass_entry.get() != confirmpass_entry.get():
            messagebox.showerror('Error','Password and Confirm Password are not matching',parent=window)
        else:
            con = pymysql.connect(host='localhost', user='root', password='tiger',database='userdata')
            mycursor = con.cursor()
            query = 'select * from data where username=%s and email=%s'
            mycursor.execute(query,(user_entry.get(),email_entry.get()))
            row=mycursor.fetchone()
            if row==None:
                messagebox.showerror('Error','Incorrect Username or Password',parent=window)

            else:
                query='update data set password=%s where username=%s and email=%s'
                mycursor.execute(query,(newpass_entry.get(),user_entry.get(),email_entry.get()))
                con.commit()
                con.close()
                messagebox.showinfo('Success','Password is reset, please login with new password',parent=window)
                window.destroy()

    window=Toplevel()

    window.resizable(False,False)
    window.title('Change Password')

    bgPic = ImageTk.PhotoImage(file='background.jpg')
    bgLabel = Label(window,image=bgPic)
    bgLabel.grid()

    heading_label = Label(window,text='RESET PASSWORD',font=('Arial',18,'bold'),
                          bg='white',fg='magenta2')
    heading_label.place(x=480,y=60)

    userLabel = Label(window,text='Username',font=('Arial',12,'bold'),
                      bg='white',fg='orchid1')
    userLabel.place(x=470,y=115)

    user_entry = Entry(window,width=25,fg='magenta2',font=('Arial',11,'bold'),
                       border=0)
    user_entry.place(x=470,y=145)

    Frame(window,width=250,height=2,bg='orchid1').place(x=470,y=165)

    emailLabel = Label(window, text='Email', font=('Arial', 12, 'bold'),
                      bg='white', fg='orchid1')
    emailLabel.place(x=470, y=180)

    email_entry = Entry(window, width=25, fg='magenta2', font=('Arial', 11, 'bold'),
                       border=0)
    email_entry.place(x=470, y=210)

    Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=230)

    passwordLabel = Label(window, text='New Password', font=('Arial', 12, 'bold'),
                      bg='white', fg='orchid1')
    passwordLabel.place(x=470, y=245)

    newpass_entry = Entry(window, width=25, fg='magenta2', font=('Arial', 11, 'bold'),
                       border=0)
    newpass_entry.place(x=470, y=275)

    Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=295)

    confirmpasswordLabel = Label(window, text='Confirm Password', font=('Arial', 12, 'bold'),
                          bg='white', fg='orchid1')
    confirmpasswordLabel.place(x=470, y=310)

    confirmpass_entry = Entry(window, width=25, fg='magenta2', font=('Arial', 11, 'bold'),
                           border=0)
    confirmpass_entry.place(x=470, y=340)

    Frame(window, width=250, height=2, bg='orchid1').place(x=470, y=360)

    submitButton = Button(window,text='Submit',bd=0,bg='magenta2',fg='white',font=('Open Sans',16,'bold'),
                          width=19,cursor='hand2',activebackground='magenta2',activeforeground='white',
                          command=change_password)
    submitButton.place(x=470,y=400)

    window.mainloop()

def login_user():
    if usernameEntry.get()=='Username'or passwordEntry.get()=='Password':
        messagebox.showerror('Error' , 'All Field Are Required')

    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='tiger')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Connection is not established try again')
            return

        query = 'use userdata'

        mycursor.execute(query)
        query='select * from data where username=%s and password=%s'
        mycursor.execute(query,(usernameEntry.get(), passwordEntry.get()))
        row=mycursor.fetchone()
        if row == None:
            messagebox.showerror('Error','Invalid username or password')
        if row is not None:
            messagebox.showinfo('Welcome','Login is successful')
            login_window.destroy()
            with open('user_data.json', 'w') as f:
                # convert the tuple to a list and then save it as a JSON
                json.dump(list(row), f)
            os.system('q.py')

def signup_page():
    login_window.destroy()
    os.system('signup.py')


def hide():
    openeye.config(file='closeye.png')
    passwordEntry.config(show='*')
    eyebutton.config(command=show)

def show():
    openeye.config(file='openeye.png')
    passwordEntry.config(show='')
    eyebutton.config(command=hide)

#GUI part
login_window = Tk()
login_window.state('zoomed')
login_window.title('BUS RESERVATION SYSTEM')
login_window.configure(bg="skyblue")
login_window.resizable(False,False)

bgImage = ImageTk.PhotoImage(file = 'bg.jpg')

txt = "Welcome to our Software"
count = 0
text = ''

label = Label(login_window,text=txt,font=('Arial',28,'bold'),fg='firebrick1',bg='skyblue')
label.place(x=520, y=40)

def slider():

    global count,text
    if count >= len(txt):
        count = -1
        text=''
        label.config(text=text)

    else:
        text = text + txt[count]
        label.config(text=text)
    count += 1

    label.after(200,slider)

slider()

bgLabel = Label(login_window ,image=bgImage)
bgLabel.place(x=250,y=80)

heading=Label(login_window,text='USER LOGIN',font=('Microsoft Yahei UI Light',23,'bold'),bg='white',fg='firebrick1')
heading.place(x=850,y=200)


def on_enter(e):
    usernameEntry.delete(0, 'end')


def on_leave(e):
    if usernameEntry.get() == '':
        usernameEntry.insert(0, 'Username')

usernameEntry = Entry(login_window,width=25,font=('Microsoft Yahei UI Light',11,'bold'),border=0,fg='firebrick1')
usernameEntry.place(x=830,y=280)
usernameEntry.insert(0, 'Username')
usernameEntry.bind("<FocusIn>", on_enter)
usernameEntry.bind("<FocusOut>", on_leave)

frame1 = Frame(login_window,width=250,height=2,bg='firebrick1')
frame1.place(x=830,y=302)

def on_enter(e):
    passwordEntry.delete(0, 'end')


def on_leave(e):
    if passwordEntry.get() == '':
        passwordEntry.insert(0, 'Password')

passwordEntry = Entry(login_window, width=25, fg='firebrick1', border=0, font=('Microsoft yaHei UI Light', 11,'bold'))
passwordEntry.place(x=830, y=340)
passwordEntry.insert(0, 'Password')
passwordEntry.bind('<FocusIn>', on_enter)
passwordEntry.bind('<FocusOut>', on_leave)

Frame(login_window, width=250, height=2, bg='firebrick1').place(x=830, y=362)

openeye=PhotoImage(file='openeye.png')
eyebutton = Button(login_window,image=openeye ,border=0 ,bg='white',activebackground='white',cursor='hand2',command=hide)
eyebutton.place(x=1050,y=335)

forgetbutton = Button(login_window,text='Forget Password?',border=0 ,bg='white',activebackground='white',
                      cursor='hand2',font=('Microsoft yaHei UI Light', 11,'bold') ,
                      fg='firebrick1',activeforeground='firebrick1',command=forget_pass)
forgetbutton.place(x=950,y=375)

loginButton = Button(login_window,text='Login',font=('Open Sans',16,'bold'),fg='white',
                     bg='firebrick1',activeforeground='white',activebackground='firebrick1',
                     cursor='hand2',border=0,width=19,command=login_user)
loginButton.place(x=825,y=430)

orLabel = Label(login_window,text='-------------- OR --------------',font=('Open Sans',16),fg='firebrick1',bg='white')
orLabel.place(x=830,y=480)

facebook_Logo = PhotoImage(file='facebook.png')
fbLabel = Label(login_window,image=facebook_Logo,bg='white')
fbLabel.place(x=885,y=518)

google_Logo = PhotoImage(file='google.png')
googleLabel = Label(login_window,image=google_Logo,bg='white')
googleLabel.place(x=935,y=518)

twitter_Logo = PhotoImage(file='twitter.png')
twitterLabel = Label(login_window,image=twitter_Logo,bg='white')
twitterLabel.place(x=985,y=518)

signLabel = Label(login_window,text="Don't have an account?",font=('Open Sans',9,'bold'),fg='firebrick1',bg='white')
signLabel.place(x=830,y=578)

newaccountButton = Button(login_window,text='Create new Account',font=('Open Sans',9,'bold underline'),fg='blue',
                     bg='white',activeforeground='blue',activebackground='white',cursor='hand2',border=0,command=signup_page)
newaccountButton.place(x=967,y=578)

login_window.mainloop()