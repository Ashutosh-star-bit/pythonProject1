import tkinter as tk
from tkinter import *
import customtkinter
from tkinter import messagebox
import json
from PIL import ImageTk,Image
import os
import pymysql

with open('passenger_detail.json', 'r') as f:
    passenger_details = json.load(f)
def proceed(*args):
    var = [var1.get(), var2.get(), var3.get(), var4.get(), var5.get()]
    tat = sum(var)
    if tat < 1:
        messagebox.showerror("Error", "Please select Payment mode")
    elif tat > 1:
        messagebox.showerror("Invalid", "Please select only one payment mode")
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
        query = 'insert into passenger(passenger_name,gender,age,journey_date,bus_type,leaving_from,going_to) value(%s,%s,%s,%s,%s,%s,%s)'
        mycursor.execute(query, (str(passenger_details[0]),str(passenger_details[1]),str(passenger_details[2]),str(passenger_details[3]),str(passenger_details[4]),str(passenger_details[5]),str(passenger_details[6])))
        con.commit()
        con.close()
        messagebox.showinfo('Success', 'Ticket is Booked successfully')
        root.destroy()
        os.system('q.py')


def open_file():
    root.destroy()
    os.system('detailpng.py')

root = tk.Tk()
root.title('Home Page')
root.state('zoomed')
root.configure(bg="#fff")
root.resizable(False,False)

main_frame = tk.Frame(root , bg="black" , pady=40)
main_frame.pack(fill=tk.BOTH ,expand=True)

img = ImageTk.PhotoImage(Image.open("border6.png").resize((1520,800)))
img1 = ImageTk.PhotoImage(Image.open("bharat-pe-logo.png").resize((100,80)),Image.LANCZOS)
img2 = ImageTk.PhotoImage(Image.open("bharatpe.png").resize((100,80)))
img3 = ImageTk.PhotoImage(Image.open("google-pay-logo.png").resize((50,50)))
img4 = ImageTk.PhotoImage(Image.open("PayPal.png").resize((130,80)))
img5 = ImageTk.PhotoImage(Image.open("paytm-icon.png").resize((100,80)))
img6 = ImageTk.PhotoImage(Image.open("phone-pe-logo.png").resize((130,90)))
# img7 = ImageTk.PhotoImage(Image.open("payment-logo.png").resize((100,80)))
img8 = ImageTk.PhotoImage(Image.open("google-icon.webp").resize((50,50)))
img9 = ImageTk.PhotoImage(Image.open("PayPal-logo.png").resize((130,80)))
img10 = ImageTk.PhotoImage(Image.open("paytm-logo.webp").resize((130,95)))
img11 = ImageTk.PhotoImage(Image.open("PhonePe_Logo.png").resize((130,88)))

border = Label(main_frame, image=img, border=0, bg='black')
border.place(x=0,y=-30)

heading = Label(main_frame,text='Payment' ,fg='#1EFFC3' ,bg="black", font=('Arial',35,'bold'))
heading.place(x=680,y=130)

var1 = tk.IntVar()

checkbox1 = tk.Checkbutton(root, image=img2,selectimage=img1, variable=var1,bg='black',activebackground='black',activeforeground='black',cursor='hand2')   #Bharat pe
checkbox1.place(x=400,y=230)

var2 = tk.IntVar()

checkbox2 = tk.Checkbutton(root, image=img6,selectimage=img11, variable=var2,bg='black',activebackground='black',activeforeground='black',cursor='hand2')   #Phone pe
checkbox2.place(x=600,y=300)

var3 = tk.IntVar()

checkbox3 = tk.Checkbutton(root, image=img5,selectimage=img10, variable=var3,bg='black',activebackground='black',activeforeground='black',cursor='hand2')    #Paytm
checkbox3.place(x=400,y=360)

var4 = tk.IntVar()

checkbox4 = tk.Checkbutton(root, image=img9, selectimage= img4 , variable=var4,bg='black',activebackground='black',activeforeground='black',cursor='hand2')    #PayPal
checkbox4.place(x=400,y=500)

var5 = tk.IntVar()
txt = '''Cash During
journey'''
checkbox5 = tk.Checkbutton(root,text=txt,fg='#7F1AFF', variable=var5,bg='black',activebackground='black',activeforeground='black',cursor='hand2',font=('Arial',24,'bold'))    #COD
checkbox5.place(x=600,y=450)

submitbutton = customtkinter.CTkButton(master=main_frame,text="Proceed" ,width=100 ,height=20 ,text_color='#1D3FFF',
                                       hover_color='#1A98FF', font=('Arial',30, 'bold'),corner_radius=50,fg_color='#17C2FF',
                                       cursor = 'hand2',command=proceed)
submitbutton.place(x=950,y=280)

backbutton = customtkinter.CTkButton(master=main_frame,text="Back" ,width=100 ,height=20 ,text_color='#1D3FFF',
                                       hover_color='#1A98FF', font=('Arial',30, 'bold'),corner_radius=50,fg_color='#17C2FF',
                                       cursor = 'hand2',command=open_file)
backbutton.place(x=950,y=380)

# var  = [var1.get(), var2.get() , var3.get() , var4.get() , var5.get()]
# tat = sum(var)
# print(tat)
root.mainloop()