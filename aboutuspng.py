from tkinter import *
from tkinter import messagebox
from PIL import ImageTk,Image
import customtkinter
import os
import tkinter as tk
from tkinter import END

def Home():
    root.destroy()
    os.system('q.py')

root = tk.Tk()
root.title('Home Page')
root.state('zoomed')
root.configure(bg="#fff")
root.resizable(False,False)

main_frame = tk.Frame(root , bg="black" , pady=40)
main_frame.pack(fill=tk.BOTH ,expand=True)

img = ImageTk.PhotoImage(Image.open("border2.png").resize((1380,700)))

border = Label(main_frame, image=img, border=0, bg='black')
border.place(x=75,y=-30)

heading = Label(main_frame,text='About our company' ,fg='#FF5E93' ,bg="black", font=('Arial',40,'bold'))
heading.place(x=680,y=120)

about_us_text = """Welcome to our ASBus Application!

    We are dedicated to providing a seamless and efficient bus booking experience for our users. 
    Our application allows you to search for buses, book tickets, and manage your reservations with ease.

    Our team is committed to ensuring that you have a pleasant journey. We value your feedback 
    and are constantly working to improve our services. ASBus is an ISO 9001:2008 certified company.

    Thank you for choosing our ASBus Application!
    """
my_frame = customtkinter.CTkScrollableFrame(main_frame,orientation="vertical",
                                            label_text=about_us_text,
                                            label_fg_color='black',label_text_color='orchid1',
                                            label_font=("Helvetica",24),
                                            border_width=0,border_color="black",fg_color="black",
                                            scrollbar_button_hover_color='white',
                                            scrollbar_button_color='black')

# Grid layout
my_frame.place(x=380,y=220)

img1= ImageTk.PhotoImage(Image.open("backbutton.png").resize((50,50)))

button8 = tk.Button(master=main_frame ,image=img1 ,border=0,borderwidth=0,bg='black',activebackground='black', cursor = 'hand2',command=Home)
button8.place(x=150 , y= 60)

root.mainloop()