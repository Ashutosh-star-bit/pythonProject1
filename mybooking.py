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

def open_file():
    root.destroy()
    os.system('q.py')

def connect_database():
    if name.get()=='' :
        messagebox.showerror('Error','Passenger name is Required')
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
        query = 'select * from passenger where journey_date=%s and passenger_name=%s '
        mycursor.execute(query, (date_entry.get(), name.get()))

        row = mycursor.fetchone()
        if row == None:
            messagebox.showerror('Error','Invalid Passenger Details')
        else:
            class DateEncoder(json.JSONEncoder):
                def default(self, obj):
                    if isinstance(obj, date):
                        return obj.isoformat()
                    return json.JSONEncoder.default(self, obj)
            with open('booking_detail.json', 'w') as f:
                json.dump(list(row), f,cls=DateEncoder)
            window = Toplevel()
            window.resizable(False, False)
            window.title('Change Password')
            def back():
                window.destroy()

            img1 = ImageTk.PhotoImage(Image.open("border5.png").resize((1380, 700)))
            bgLabel = Label(window, image=img1,bg='white')
            bgLabel.grid()
            with open('booking_detail.json', 'r') as f:
                booking_details = json.load(f)
            heading0 = Label(window, text='Booking Details', fg='red', bg="white", font=('Arial', 24, 'bold'))
            heading0.place(x=560, y=100)
            heading1 = Label(window, text='Passenger Name:', fg='yellow', bg="white", font=('Arial', 24, 'bold'))
            heading1.place(x=200, y=180)
            details1 = tk.Label(window, text="" + str(booking_details[1]), font=('Arial Rounded MT Bold', 24, 'bold'),
                                fg="skyblue", bg='white')
            details1.place(x=470, y=180)
            heading2 = Label(window, text='Gender:', fg='yellow', bg="white", font=('Arial', 24, 'bold'))
            heading2.place(x=200, y=260)
            details2 = tk.Label(window, text="" + str(booking_details[2]), font=('Arial Rounded MT Bold', 24, 'bold'),
                                fg="skyblue", bg='white')
            details2.place(x=330, y=260)
            heading3 = Label(window, text='Age:', fg='yellow', bg="white", font=('Arial', 24, 'bold'))
            heading3.place(x=200, y=340)
            details3 = tk.Label(window, text="" + str(booking_details[3]), font=('Arial Rounded MT Bold', 24, 'bold'),
                                fg="skyblue", bg='white')
            details3.place(x=280, y=340)
            heading4 = Label(window, text='Date of Journey:', fg='yellow', bg="white", font=('Arial', 24, 'bold'))
            heading4.place(x=200, y=420)
            details4 = tk.Label(window, text="" + str(booking_details[4]), font=('Arial Rounded MT Bold', 24, 'bold'),
                                fg="skyblue", bg='white')
            details4.place(x=460, y=420)
            heading5 = Label(window, text='Bus type:', fg='yellow', bg="white", font=('Arial', 24, 'bold'))
            heading5.place(x=750, y=180)
            details5 = tk.Label(window, text="" + str(booking_details[5]), font=('Arial Rounded MT Bold', 24, 'bold'),
                                fg="skyblue", bg='white')
            details5.place(x=900, y=180)

            heading6 = Label(window, text='Leaving place:', fg='yellow', bg="white", font=('Arial', 24, 'bold'))
            heading6.place(x=750, y=260)
            details6 = tk.Label(window, text="" + str(booking_details[6]), font=('Arial Rounded MT Bold', 24, 'bold'),
                                fg="skyblue", bg='white')
            details6.place(x=980, y=260)
            heading7 = Label(window, text='Destination place:', fg='yellow', bg="white", font=('Arial', 24, 'bold'))
            heading7.place(x=750, y=340)
            details7 = tk.Label(window, text="" + str(booking_details[7]), font=('Arial Rounded MT Bold', 24, 'bold'),
                                fg="skyblue", bg='white')
            details7.place(x=1035, y=340)

            heading8 = Label(window, text='Payment Status:', fg='yellow', bg="white", font=('Arial', 24, 'bold'))
            heading8.place(x=750, y=420)
            details8 = tk.Label(window, text="" + str(booking_details[8]), font=('Arial Rounded MT Bold', 24, 'bold'),
                                fg="skyblue", bg='white')
            details8.place(x=1005, y=420)
            backbutton = customtkinter.CTkButton(master=window, text="Back", width=100, height=20, text_color='red',
                                                 hover_color='#1A98FF', font=('Arial', 30, 'bold'), corner_radius=50,
                                                 cursor='hand2', command=back)
            backbutton.place(x=630, y=500)
            window.mainloop()
        con.commit()
        con.close()


root = tk.Tk()
root.title('Home Page')
root.state('zoomed')
root.configure(bg="#fff")
root.resizable(False,False)

main_frame = tk.Frame(root , bg="black" , pady=40)
main_frame.pack(fill=tk.BOTH ,expand=True)

img = ImageTk.PhotoImage(Image.open("border5.png").resize((1380,700)))

border = Label(main_frame, image=img, border=0, bg='black')
border.place(x=85,y=0)

heading = Label(main_frame,text='My Booking' ,fg='#1EFFC3' ,bg="black", font=('Arial',35,'bold'))
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

img2= ImageTk.PhotoImage(Image.open("backbutton.png").resize((50,50)))

button8 = tk.Button(master=main_frame ,image=img2 ,border=0,borderwidth=0,bg='black',activebackground='black', cursor = 'hand2',command=open_file)
button8.place(x=450 , y=120)

root.mainloop()