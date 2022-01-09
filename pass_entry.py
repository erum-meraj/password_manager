


def pass_entry(usid): 
    import tkinter as tk
    #import requests # Download this library using pip install request!!!!!!!
    from tkinter import font
    import mysql.connector as sql
    from pass_entry_db_con import add_pass_to_db
    #root app
    root = tk.Toplevel()
    root.title("Password Manager")
    root.configure(background = "#7c898b")
    root.minsize(height=982, width=700)

    #sql connection 
    con = sql.connect(host = 'localhost', user = 'root', password = 'erummeraj', database = 'pw-manager')
    cur = con.cursor(buffered=True)

    #layout
    frame = tk.Frame(root, bg="#d9d9d9", bd=5)
    frame.place(x=115 , y = 170 , height = 630 , width =450)

    background_image= tk.PhotoImage(file=r'/Users/momeraj/Documents/erum/learning-python-master/12th/Password-Manager-master/Logo-removebg-preview.png')
    background_label = tk.Label(root, image=background_image, bg = "#d9d9d9")
    background_label.place(x=140, y=180, width=400, height=200)


    welcomeback=tk.Label(frame,text = "NEW PASSWORD", font=("times new roman" , 35 , "bold") , fg = "black", bg = "#d9d9d9")
    welcomeback.place(x=80 , y =250)

    username=tk.Label(frame,text = "Username", font=("times new roman" , 24 , "bold") , fg = "black", bg = "#d9d9d9")
    username.place(x= 80  , y =320)

    entry_username = tk.Entry(frame, font=('Bookman Old Style', 18), bg="white", fg="black")
    entry_username.place(x=80  , y =350 , width = 270)

    password=tk.Label(frame,text = "Password", font=("times new roman" , 24 , "bold") , fg = "black", bg = "#d9d9d9")
    password.place(x= 80  , y =400)

    bullet = "\u2022" 
    entry_password = tk.Entry(frame, font=('Bookman Old Style', 18), bg="white", fg="black", show=bullet)
    entry_password.place(x= 80  , y =430, width = 270)

    note=tk.Label(frame,text = "Note", font=("times new roman" , 24 , "bold") , fg = "black", bg = "#d9d9d9")
    note.place(x= 80  , y =480)


    entry_note = tk.Entry(frame, font=('Bookman Old Style', 18), bg="white", fg="black")
    entry_note.place(x= 80  , y =510 , width = 270, height= 60)

    button_login = tk.Button(frame, text="Add PW", font=('Bookman Old Style', 14), bg='#ffffff', fg="black" , command=lambda: add_pass_to_db(entry_username.get(), entry_password.get(), entry_note.get(), usid, cur , con))
    button_login.place(x=155,y=580, height=35, width=120)

    root.mainloop()