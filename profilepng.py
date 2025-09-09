from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import customtkinter
import os
import tkinter as tk
from tkinter import END
import json

def Home():
    root.destroy()
    os.system('q.py')


root = tk.Tk()
root.title('Profile Page')
root.state('zoomed')
root.configure(bg="#fff")
root.resizable(False,False)

main_frame = tk.Frame(root , bg="black" , pady=40)
main_frame.pack(fill=tk.BOTH ,expand=True)

img = ImageTk.PhotoImage(Image.open("border4.jpg").resize((1480,850)))

border = Label(main_frame, image=img, border=0, bg='black')
border.place(x=35,y=-65)

heading = Label(main_frame,text='Profile' ,fg='springgreen' ,bg="black", font=('Arial',40,'bold'))
heading.place(x=680,y=180)

with open('user_data.json', 'r') as f:
    user_details = json.load(f)

heading1 = Label(main_frame,text='Username:' ,fg='yellow' ,bg="black", font=('Arial',24,'bold'))
heading1.place(x=380,y=320)
details1 = tk.Label(main_frame, text="" + str(user_details[2]), font=('Arial Rounded MT Bold',24,'bold'),fg="skyblue",bg='black')
details1.place(x=570,y=320)

heading2 = Label(main_frame,text='Email:' ,fg='yellow' ,bg="black", font=('Arial',24,'bold'))
heading2.place(x=850,y=320)
details2 = tk.Label(main_frame, text="" + str(user_details[1]), font=('Arial Rounded MT Bold',24,'bold'),fg="skyblue",bg='black')
details2.place(x=980,y=320)

img1= ImageTk.PhotoImage(Image.open("backbutton.png").resize((50,50)))

button = tk.Button(master=main_frame ,image=img1 ,border=0,borderwidth=0,bg='black',activebackground='black', cursor = 'hand2',command=Home )
button.place(x=450 , y= 190)

root.mainloop()