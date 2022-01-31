def user_record_entry(name , passw, mail, cur, con):

    if name == "" or passw == "" or mail == "":
        print("Pls fill all the details ") 
        return 0
    else:
        
        name_entered = name
        pw_entered = passw
        email_entered = mail
        query = "INSERT INTO users( username, password, email ) VALUES('{}', '{}', '{}')".format(name_entered, pw_entered, email_entered)
        try:
            cur.execute(query)
            
            con.commit()
            print("registration successful ")
            return 1
        except :
            print("registration failed ")
            return 2
    con.close()
