from pass_entry import pass_entry


def add_pass_to_db(name , passw, note, usid, cur, con):
    print("hello from the other side")
    if name == "" or passw == "" or note == "":
            print("Pls fill all the details ") 
    else:
        
        name_entered = name
        pw_entered = passw
        note_entered = note
        query = "INSERT INTO passw( user_id , website , password, descrip ) VALUES('{}', '{}', '{}')".format(usid, name_entered, pw_entered, note_entered)
        try:
            cur.execute(query)
            con.commit()
            print("registration successful ")
        except :
            print("registration failed ")
    con.close()

    return