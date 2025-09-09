import tkinter as tk
from tkinter import *
import customtkinter
from PIL import ImageTk,Image
import json

def back():
    window.destroy()
# window = Toplevel()
window = tk.Tk()
window.resizable(False, False)
window.title('Change Password')
img1 = ImageTk.PhotoImage(Image.open("border5.png").resize((1380, 700)))
# bgPic = ImageTk.PhotoImage(file='background.jpg')
bgLabel = Label(window, image=img1,bg='white')
bgLabel.grid()
with open('booking_detail.json', 'r') as f:
    booking_details = json.load(f)
heading0 = Label(window, text='Booking Details:', fg='yellow', bg="white", font=('Arial', 24, 'bold'))
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
backbutton = customtkinter.CTkButton(master=window,text="Back" ,width=100 ,height=20 ,text_color='red',
                                       hover_color='#1A98FF', font=('Arial',30, 'bold'),corner_radius=50,
                                       cursor = 'hand2',command=back)
backbutton.place(x=630,y=500)
window.mainloop()