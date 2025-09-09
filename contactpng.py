from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import customtkinter
import pymysql
import os
import tkinter as tk
from tkinter import END

def Home():
    root.destroy()
    os.system('q.py')

def comment_submit ():
    comment = comment_text.get("1.0", "end-1c")  # Get text from Text widget
    print(f"User comment: {comment}")  # Print comment or do something with it
    if usernameEntry.get()==''or usernameEmail.get()=='':
        messagebox.showerror('Error' , 'All Field Are Required')

    elif comment_text.get("1.0", "end-1c")=='':
        messagebox.showerror('Error','Please leave a comment')

    else:
        try:
            con=pymysql.connect(host='localhost',user='root',password='tiger')
            mycursor=con.cursor()
        except:
            messagebox.showerror('Error','Connection is not established try again')
            return

        query = 'use userdata'

        mycursor.execute(query)
        query='select * from data where username=%s and email=%s'
        mycursor.execute(query,(usernameEntry.get(), usernameEmail.get()))
        row=mycursor.fetchone()
        if row == None:
            messagebox.showerror('Error','Invalid Username or Email')
        else:
            try:
                con = pymysql.connect(host='localhost', user='root', password='tiger')
                mycursor = con.cursor()
            except:
                messagebox.showerror('Error', 'Database Connectivity Issue, Please Try Again')
                return

            try:
                query = 'create database userdata'
                mycursor.execute(query)
                query = 'use userdata'
                mycursor.execute(query)
                query = 'create table commentdata(id int auto_increment primary key not null,username varchar(100),email varchar(50),comment varchar(10000))'
                mycursor.execute(query)
            except:
                query='use userdata'
                mycursor.execute(query)
                query = 'insert into commentdata(username,email,comment) value(%s,%s,%s)'
                mycursor.execute(query, (usernameEntry.get(), usernameEmail.get(),comment_text.get("1.0", "end-1c")))
                con.commit()
                con.close()
                comment_text.delete("1.0", tk.END)
                usernameEntry.delete(0, END)
                usernameEmail.delete(0, END)
                messagebox.showinfo('Success', 'Comment submitted successful')



root = tk.Tk()
root.title('Home Page')
root.state('zoomed')
root.configure(bg="#fff")
root.resizable(False,False)

main_frame = tk.Frame(root , bg="black" , pady=40)
main_frame.pack(fill=tk.BOTH ,expand=True)

img = ImageTk.PhotoImage(Image.open("border3.jpg").resize((1380,700)))

border = Label(main_frame, image=img, border=0, bg='black')
border.place(x=75,y=-30)

heading = Label(main_frame,text='Contact us' ,fg='#FF713F' ,bg="black", font=('Arial',40,'bold'))
heading.place(x=850,y=60)

contact_us_text = """You Can reach out to us for any service 
  related queries """

heading1 = Label(main_frame,text=contact_us_text ,fg='skyblue' ,bg="black", font=('Arial',24,'bold'))
heading1.place(x=700,y=150)

usernameEntry = customtkinter.CTkEntry(main_frame,placeholder_text='User Name',border_width=0,width=330,height=40,bg_color='black',fg_color='white',placeholder_text_color="orange",
                                       text_color="black",font=('Arial',18,'bold'))
usernameEntry.place(x=810,y=280)

usernameEmail = customtkinter.CTkEntry(main_frame,placeholder_text='User Email',border_width=0,width=330,height=40,bg_color='black',fg_color='white',placeholder_text_color="orange",
                                       text_color="black",font=('Arial',18,'bold'))
usernameEmail.place(x=810,y=345)

heading2 = Label(main_frame,text='Leave Comment' ,fg='skyblue' ,bg="black", font=('Arial',22,'bold'))
heading2.place(x=810,y=395)

comment_text = tk.Text(root, width=30, height=7,font=('Arial',14,'bold'))
comment_text.place(x=810,y=475)

img1= ImageTk.PhotoImage(Image.open("backbutton.png").resize((50,50)))

button = tk.Button(master=main_frame ,image=img1 ,border=0,borderwidth=0,bg='black',activebackground='black', cursor = 'hand2',command=Home )
button.place(x=600 , y= 60)

submitbutton = customtkinter.CTkButton(master=main_frame,text="Submit" ,width=100 ,height=20 ,text_color='red',
                                       hover_color='#1A98FF', font=('Arial',30, 'bold'),corner_radius=50,
                                       cursor = 'hand2',command=comment_submit)
submitbutton.place(x=900,y=650)

heading3 = Label(main_frame,text='Email:' ,fg='#1A98FF' ,bg="black", font=('Arial',22,'bold'))
heading3.place(x=150,y=520)

heading4 = Label(main_frame,text='Phone:' ,fg='#1A98FF' ,bg="black", font=('Arial',22,'bold'))
heading4.place(x=150,y=620)

heading5 = Label(main_frame,text='support@ASBus.com' ,fg='#1A98FF' ,bg="black", font=('Arial',22,'bold'))
heading5.place(x=175,y=570)

heading4 = Label(main_frame,text='040-6165XXXX' ,fg='#1A98FF' ,bg="black", font=('Arial',22,'bold'))
heading4.place(x=175,y=670)

root.mainloop()