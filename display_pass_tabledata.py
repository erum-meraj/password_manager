import mysql.connector as sql
from mysql.connector.utils import read_int
def check_data(id, cur):
    query = "select website, password, descrip from passw where user_id = '{}' ".format(id)
    cur.execute(query)
    data = cur.fetchall()
    record = []
    for i in range(0, len(data)):
        record.append(list(data[i]))
    return record