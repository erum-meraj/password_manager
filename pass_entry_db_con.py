
def add_pass_to_db(website, passw, note, usid, cur, con):
    print("hello from the other side")
    if website == "" or passw == "" or note == "":
            print("Pls fill all the details ") 
    else:
        
        website_entered = website
        pw_entered = passw
        note_entered = note
        query = "INSERT INTO passw( user_id , website , password, descrip ) VALUES('{}', '{}', '{}', '{}')".format(usid, website_entered, pw_entered, note_entered)
        try:
            cur.execute(query)
            print("query is good")
            con.commit()
            print("registration successful ")
        except :
            print("registration failed ")
    con.close()

    return