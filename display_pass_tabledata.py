import mysql.connector as sql
from mysql.connector.utils import read_int
def check_data(id, cur):
    query = "select * from passw where user_id = '{}' ".format(id)
    cur.execute(query)
    data = cur.fetchall()
    record  = list(data[0])
    return record

