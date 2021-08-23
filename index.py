import tkinter as tk
#import requests # Download this library using pip install request!!!!!!!
from tkinter import font
import mysql.connector as sql
from reg_user import user_record_check
from PIL import Image, ImageTk # Download this library using pip install Pillow!!!!!


#root app
root = tk.Tk()
root.title("Password Manager")
root.configure(background = "#f8eded")
root.minsize(height=982, width=700)

#sql connection 
con = sql.connect(host = 'localhost', user = 'root', password = 'erummeraj', database = 'pw-manager')
cur = con.cursor(buffered=True)

#sign_up_redirect_function
def sign_up_redirect():
    import signup


#layout
frame = tk.Frame(root, bg="#FADCD9", bd=5)
frame.place(x=115 , y = 170 , height = 630 , width =450)

background_image= tk.PhotoImage(file=r'/Users/momeraj/Documents/erum/learning-python-master/12th/Password-Manager-master/Logo-removebg-preview.png')
background_label = tk.Label(root, image=background_image, bg = "#FADCD9")
background_label.place(x=140, y=180, width=400, height=200)


welcomeback=tk.Label(frame,text = "WELCOME BACK!", font=("times new roman" , 35 , "bold"-) , fg = "black", bg = "#FADCD9")
welcomeback.place(x=70 , y =260)

username=tk.Label(frame,text = "Username", font=("times new roman" , 24 , "bold") , fg = "black", bg = "#FADCD9")
username.place(x= 80  , y =330)

entry_username = tk.Entry(frame, font=('Bookman Old Style', 18), bg="white", fg="black")
entry_username.place(x=80  , y =360 , width = 270)

password=tk.Label(frame,text = "Password", font=("times new roman" , 24 , "bold") , fg = "black", bg = "#FADCD9")
password.place(x= 80  , y =420)

bullet = "\u2022" 
entry_password = tk.Entry(frame, font=('Bookman Old Style', 18), bg="white", fg="black", show=bullet)
entry_password.place(x= 80  , y =450 , width = 270)

button_login = tk.Button(frame, text="Login", font=('Bookman Old Style', 14), bg='#ffffff', fg="black" , command=lambda: user_record_check(entry_username.get(), entry_password.get(), cur))
button_login.place(x=155,y=510, height=35, width=120)

link1 = tk.Label(frame, text="Don't have an account?? Sign Up", fg="#787A91", font=('Bookman Old Style', 14,'underline'), cursor="hand2", bg= "#FADCD9")
link1.place(x=120,y=560)
link1.bind("<Button-1>", lambda e: sign_up_redirect())


#sign_up_redirect

root.mainloop()