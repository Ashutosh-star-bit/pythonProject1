from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import customtkinter
import re
import json
import os
import tkinter as tk
from tkinter import END
def cancelbook():
    root.destroy()
    os.system('cancelbooking.py')
def booking():
    root.destroy()
    os.system('mybooking.py')
def profile():
    root.destroy()
    os.system('profilepng.py')
def contact():
    root.destroy()
    os.system('contactpng.py')
def about():
    root.destroy()
    os.system('aboutuspng.py')

def logout():
    root.destroy()
    os.system('signin.py')

root = tk.Tk()
root.title('Home Page')
root.state('zoomed')
root.configure(bg="#fff")
root.resizable(False,False)
colour1 = '#020f12'
colour2 = '#05d7ff'
colour3 = '#65e7ff'
colour4 = 'BLACK'
colour5 = '#BC62FF'

main_frame = tk.Frame(root , bg="black" , pady=40)
main_frame.pack(fill=tk.BOTH ,expand=True)

img1 = customtkinter.CTkImage(Image.open("Home icon1.png").resize((50,50)))
img2 = customtkinter.CTkImage(Image.open("my bus booking.png").resize((20,20)))
img3 = customtkinter.CTkImage(Image.open("Cancel Booking.png").resize((20,20)))
img4 = customtkinter.CTkImage(Image.open("Contact icon1.png").resize((20,20)))
img5 = customtkinter.CTkImage(Image.open("About icon.png").resize((20,20)))
img6 = customtkinter.CTkImage(Image.open("Profile icon.jpg").resize((20,20)))
img7 = customtkinter.CTkImage(Image.open("Logout icon.jpg").resize((20,20)))
img8 = customtkinter.CTkImage(Image.open("bus photo.png").resize((20,20)))
img9 = ImageTk.PhotoImage(Image.open("border home.png").resize((1380,700)))
img10 = customtkinter.CTkImage(Image.open("Interchange icon.png").resize((500,500)))

border = Label(main_frame, image=img9, border=0, bg='black')
border.place(x=85,y=-50)

heading = Label(main_frame,text='Home' ,fg='springgreen' ,bg="black", font=('Arial',40,'bold'))
heading.place(x=680,y=30)


button1 = customtkinter.CTkButton(master=main_frame,image=img1 ,text="Home" ,width=100 ,height=20,compound="top",fg_color='black',text_color='red',hover_color='#1A98FF', font=('Arial',30, 'bold') ,corner_radius=50, cursor = 'hand2')
button1.place(x=25,y= 700)

button2 = customtkinter.CTkButton(master=main_frame,image=img3,text="Cancel Booking" ,width=100 ,height=20 ,compound="top",fg_color='black',text_color='red',hover_color='#1A98FF', font=('Arial',26, 'bold'),corner_radius=50, cursor = 'hand2',command=cancelbook)
button2.place(x=430,y= 700)

button3 = customtkinter.CTkButton(master=main_frame,image=img2,text="My Booking" ,width=100 ,height=20 ,compound="top",fg_color='black',text_color='red',hover_color='#1A98FF', font=('Arial',26, 'bold'),corner_radius=50, cursor = 'hand2',command=booking)
button3.place(x=200,y= 700)

button4 = customtkinter.CTkButton(master=main_frame,image=img6,text="Profile" ,width=100 ,height=20 ,compound="top",fg_color='black',text_color='red',hover_color='#1A98FF', font=('Arial',30, 'bold'),corner_radius=50, cursor = 'hand2',command=profile)
button4.place(x=720,y=700)

button5 = customtkinter.CTkButton(master=main_frame,image=img4,text="Contact us" ,width=100 ,height=20 ,compound="top",fg_color='black',text_color='red',hover_color='#1A98FF', font=('Arial',30, 'bold'),corner_radius=50, cursor = 'hand2',command=contact)
button5.place(x=900,y= 700)

button6 = customtkinter.CTkButton(master=main_frame,image=img5,text="About Us" ,width=100 ,height=20 ,compound="top",fg_color='black',text_color='red',hover_color='#1A98FF', font=('Arial',30, 'bold'),corner_radius=50, cursor = 'hand2',command=about)
button6.place(x=1150,y= 700)

button7 = customtkinter.CTkButton(master=main_frame,image=img7,text="Log Out" ,width=100 ,height=20 ,compound="top",fg_color='black',text_color='red',hover_color='#1A98FF', font=('Arial',30, 'bold'),corner_radius=50, cursor = 'hand2',command=logout)
button7.place(x=1350,y= 700)

font1 = ('Times',18,'italic')
my_list = ['Mirzapur' ,'Prayagraj' ,'Kanpur','Varanasi','Lucknow','Bareilly','Lucknow','Agra','Sonbhadra']
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
e1.place(x=400,y=250)
e1.insert(0,'Leaving from')
e1.bind('<FocusIn>' , on_enter)
e1.bind('<FocusOut>',on_leave)
l1 = tk.Listbox(main_frame,height=4,width=15,font=font1,relief='solid' ,bg='black' ,fg="#1A98FF",border=0,highlightthickness=0)
l1.place(x=400,y=285)
def on_enter(e):
    e2.delete(0,'end')
def on_leave(e):
    if e2.get()=='':
        e2.insert(0,'Going to')

e2_str = tk.StringVar()
e2 = tk.Entry(main_frame,font=font1,textvariable=e2_str ,fg='#1A98FF')
e2.place(x=850,y=250)
e2.insert(0,'Going to')
e2.bind('<FocusIn>' , on_enter)
e2.bind('<FocusOut>',on_leave)
l2 = tk.Listbox(main_frame,height=4,width=15,font=font1,relief='flat' ,bg='black' ,highlightthickness=0 ,fg="#1A98FF",border=0)
l2.place(x=850,y=285)
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
def bus_ticket(*args):
    if e1.get() == 'Leaving from' and e2.get() == 'Going to':
        messagebox.showerror('Invalid', 'Please select your Origin City and Destination')

    elif e1.get() == 'Leaving from':
        messagebox.showerror('Invalid', 'Please select your Origin City')

    elif e2.get() == 'Going to':
        messagebox.showerror('Invalid','Please select your Destination')

    elif e2.get() == e1.get() :
        messagebox.showerror('Invalid', "Both Place should be different")
    else:
        # Combine data into a dictionary
        data = [e1.get(),e2.get()]

        # Write data to a JSON file
        with open('user_input.json', 'w') as f:
            json.dump(list(data),f)

        root.destroy()
        os.system('detailpng.py')
def interchange_text():
    if e1.get() == 'Leaving from' and e2.get() == 'Going to':
        messagebox.showerror('Invalid', 'Please select your Origin City and Destination')

    elif e1.get() == 'Leaving from':
        messagebox.showerror('Invalid', 'Please select your Origin City')

    elif e2.get() == 'Going to':
        messagebox.showerror('Invalid', 'Please select your Destination')

    elif e2.get() == e1.get():
        messagebox.showerror('Invalid', "Both Place should be different")
    else:
        box1_text = e1.get()
        box2_text = e2.get()

        e1.delete(0, tk.END)
        e1.insert(0, box2_text)

        e2.delete(0, tk.END)
        e2.insert(0, box1_text)
button8 = customtkinter.CTkButton(master=main_frame,text="Book Bus Tickets" ,width=245 ,height=20 ,compound="left",fg_color='#1A98FF',text_color='black',hover_color='blue', font=('Arial',24, 'italic'),corner_radius=50, cursor = 'hand2',command=bus_ticket)
button8.place(x=630 , y= 350)

button9 = customtkinter.CTkButton( master=main_frame ,image=img10,fg_color='black',hover_color='white', cursor = 'hand2',width=0 ,text="" ,command=interchange_text)
button9.place(x=730,y=250)

# print(main_frame['bg'])
root.mainloop()