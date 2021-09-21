import mysql.connector as sql
def check_data(id, cur):
    query = "select * from passw where user_id = '{}' ".format(id)
    cur.execute(query)
    data = cur.fetchall()
    print(data)

con = sql.connect(host = 'localhost', user = 'root', password = 'erummeraj', database = 'pw-manager')
cur = con.cursor(buffered=True)

userid = 1
data = check_data(userid, cur) 