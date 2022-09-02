import sys
import os
import mysql.connector
from dotenv import load_dotenv
#import traceback
#import json
sys.path.append('..')

# connect to local db goodreadscrape
def get_cursor_db():
    load_dotenv()
    mydb = mysql.connector.connect(
    host="localhost",
    user=os.getenv('USER'),
    password=os.getenv('PASSWORD'),
    database="242_final_project"
    )
    mycursor = mydb.cursor() # mysql db cursor
    return mycursor, mydb