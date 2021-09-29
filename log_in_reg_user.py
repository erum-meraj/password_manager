def user_record_check(name, passw, cur):
    name_entered = name
    pw_entered = passw
    #query = "SELECT username, password, COUNT(*) FROM users WHERE username = {} and password = {}".format(name_entered, pw_entered)
    query = "select username, password from users where username = '{}' and password = '{}'".format(name_entered, pw_entered)
    cur.execute(query)
    data = cur.fetchall()
    lines = 0
    for l in data:
        lines = lines + 1
    print(lines)
    if lines == 0:
        print ("It Does Not Exist")   
    else:
        print("Exists")
    #con.close();
    return