
def add_pass_to_db(website, passw, note, usid, cur, con):
    print("hello from the other side")
    if website == "" or passw == "" or note == "":
            print("Pls fill all the details ") 
            return 2
    else:
        
        website_entered = website
        pw_entered = passw
        note_entered = note
        query = "INSERT INTO passw( user_id , website , password, descrip ) VALUES('{}', '{}', '{}', '{}')".format(usid, website_entered, pw_entered, note_entered)
        try:
            cur.execute(query)
            con.commit()
            print("registration successful ")
            return 1
        except :
            print("registration failed ")
            return 0
    con.close()

    return