import tkinter as tk
import tksheet
#import requests # Download this library using pip install request!!!!!!!
from tkinter import font
import mysql.connector as sql
from table_data import check_data
from PIL import Image, ImageTk # Download this library using pip install Pillow!!!!!


#root app
root = tk.Tk()
root.title("Password Manager")
root.configure(background = "#f8eded")
root.minsize(height=982, width=700)

#sql connection 
con = sql.connect(host = 'localhost', user = 'root', password = 'erummeraj', database = 'pw-manager')
cur = con.cursor(buffered=True)


#layout
frame = tk.Frame(root, bg="#FADCD9", bd=5)
frame.place(x=115 , y = 170 , height = 630 , width =450)

background_image= tk.PhotoImage(file=r'/Users/momeraj/Documents/erum/learning-python-master/12th/Password-Manager-master/Logo-removebg-preview.png')
background_label = tk.Label(root, image=background_image, bg = "#FADCD9")
background_label.place(x=140, y=180, width=400, height=200)


welcomeback=tk.Label(frame,text = "WELCOME BACK!", font=("times new roman" , 35 , "bold") , fg = "black", bg = "#FADCD9")
welcomeback.place(x=70 , y =260)


#table
userid = 1
sheet1 = tksheet.Sheet(frame, width=380, height=160, total_columns=4, show_x_scrollbar=True, show_y_scrollbar=True)
sheet1.place( x = 40, y = 320)
data = check_data(userid, cur) 
sheet1.headers(["user_id","website","password","note"])
sheet1.set_sheet_data(data = [[1, "https://www.google.com", "erummeraj", "dont forget this"]])
sheet1.enable_bindings(("single_select","row_select","column_width_resize","arrowkeys","rc_select","copy","cut","paste",))
a = sheet1.get_cell_data(2, 1)               
text = str(a)
root.mainloop()