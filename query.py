import mysql.connector 
import streamlit as st

#connection 
conn = mysql.connector.connect(
    host="localhost",
    port="4306",
    user="root",
    passwd="",
    db="myDb"
)

c = conn.cursor()

#fetch the data

def view_all_data():
    c.execute("select * from insurance order by id asc")
    data = c.fetchall()
    return data


