import tkinter as tk
import requests # Download this library using pip install request!!!!!!!
from tkinter import font
import webbrowser
from PIL import Image, ImageTk # Download this library using pip install Pillow!!!!!
root = tk.Tk()
root.title("Password Manager")
root.configure(background = "mediumturquoise")
root.minsize(height=1056, width=1441)

def hello():
    print("hello")

frame = tk.Frame(root, bg="lightpink", bd=5)
frame.place(x=500 , y = 170 , height = 630 , width =450)

background_image= tk.PhotoImage(file=r'/Users/momeraj/Documents/erum/learning-python-master/12th/Password-Manager-master/Logo-removebg-preview.png')
background_label = tk.Label(root, image=background_image, bg = "lightpink")
background_label.place(x=725, y=180, width=400, height=200, anchor='n')


welcomeback=tk.Label(frame,text = "WELCOME BACK!", font=("times new roman" , 35 , "bold") , fg = "black", bg = "lightpink")
welcomeback.place(x=70 , y =260)

username=tk.Label(frame,text = "Username", font=("times new roman" , 24 , "bold") , fg = "black", bg = "lightpink")
username.place(x= 80  , y =330)

entry_username = tk.Entry(frame, font=('Bookman Old Style', 18), bg="white", fg="black")
entry_username.place(x=80  , y =360 , width = 270)

password=tk.Label(frame,text = "Password", font=("times new roman" , 24 , "bold") , fg = "black", bg = "lightpink")
password.place(x= 80  , y =420)

entry_username = tk.Entry(frame, font=('Bookman Old Style', 18), bg="white", fg="black")
entry_username.place(x= 80  , y =450 , width = 270)

button_login = tk.Button(frame, text="Login", font=('Bookman Old Style', 14), bg='#ffffff', fg="black" )
button_login.place(x=155,y=510, height=35, width=120)
print("Don't have an account?? \033[4mSign Up\033[0m")
link1 = tk.Label(frame, text="Don't have an account?? Sign Up", fg="#787A91", font=('Bookman Old Style', 14,'underline'), cursor="hand2", bg= "lightpink")
link1.place(x=120,y=560)
link1.bind("<Button-1>", lambda e: hello())


#sign_up_redirect

'''
frame = tk.Frame(root, bg="paleturquoise", bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=('Bookman Old Style', 18))
entry.place(relwidth=0.65, relheight=1)


button = tk.Button(frame, text="Get Weather", font=('Bookman Old Style', 14), command=lambda: weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)


lower_frame = tk.Frame(root, bg='paleturquoise', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')


label = tk.Label(lower_frame, justify='left')
label.place(relwidth=1, relheight=1)


results = tk.Label(lower_frame, anchor='nw', justify='left', bd=4)
results.config(font=('Bookman Old Style', 19), bg='#ffffff')


results.place(relwidth=1, relheight=1)

weather_icon = tk.Canvas(results, bg='#ffffff', bd=0, highlightthickness=0)
weather_icon.place(relx=.6, rely=0, relwidth=1, relheight=0.5)



'''




root.mainloop()






