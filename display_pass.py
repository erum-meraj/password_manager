


def display_table(userid):
     
    import tkinter as tk
    import tksheet
    from tkinter import font
    import mysql.connector as sql
    from display_pass_tabledata import check_data
    from pass_entry import pass_entry


    #root app
    root = tk.Toplevel()
    root.title("Password Manager")
    root.configure(background = "#7c898b")
    root.minsize(height=982, width=700)

    #sql connection 
    con = sql.connect(host = 'localhost', user = 'root', password = 'erummeraj', database = 'pw-manager')
    cur = con.cursor(buffered=True)
    def  table():
        sheet1 = tksheet.Sheet(frame, width=380, height=160, total_columns=4, show_x_scrollbar=True, show_y_scrollbar=True, theme = "light green")
        sheet1.place( x = 40, y = 320)
        data = check_data(userid, cur) 

        sheet1.headers(["website","password","note"])
        sheet1.set_sheet_data(data = data)
        sheet1.enable_bindings(("single_select","row_select","column_width_resize","arrowkeys","rc_select","copy","cut","paste", "edit_cell", "rc_insert_row"))
    



    #layout
    frame = tk.Frame(root, bg="#d9d9d9", bd=5)
    frame.place(x=115 , y = 170 , height = 630 , width =450)

    background_image= tk.PhotoImage(file=r'/Users/momeraj/Documents/erum/learning-python-master/12th/split_code my exp/Logo-removebg-preview.png')
    background_label = tk.Label(root, image=background_image, bg = "#d9d9d9")
    background_label.place(x=140, y=180, width=400, height=200)


    welcomeback=tk.Label(frame,text = "PASSWORDS!", font=("times new roman" , 35 , "bold") , fg = "black", bg = "#d9d9d9")
    welcomeback.place(x=70 , y =260)

    button_login = tk.Button(frame, text="Add new password", font=('Bookman Old Style', 14), bg='#ffffff', fg="black" , command=lambda: pass_entry(userid))
    button_login.place(x=140,y=510, height=35, width= 200)
    table()

    
    
    root.mainloop()
