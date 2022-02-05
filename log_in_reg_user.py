def user_record_check(name, passw, cur):
    from display_pass import display_table
    name_entered = name
    pw_entered = passw
    #query = "SELECT username, password, COUNT(*) FROM users WHERE username = {} and password = {}".format(name_entered, pw_entered)
    query = "select id from users where username = '{}' and password = '{}'".format(name_entered, pw_entered)
    cur.execute(query)
    data = cur.fetchall()
    lines = 0
    for l in data:
        lines = lines + 1
    if lines == 0:
        print ("It Does Not Exist") 
        return 0   
    else:
        print("Exists")
        print(data)
        display_table(data[0][0])
        return 1
    #con.close();
    