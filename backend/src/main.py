"""main.py is used for running the terminal interface
for database cleaning & querying."""

#import flask
import os
#import io
import sys
import mysql.connector
#import traceback
#import json
sys.path.append('..')
#from flask import request
#from flask_cors import CORS, cross_origin
from dotenv import load_dotenv
#from contextlib import redirect_stdout
import database
from terminal import *
from helper import commit_change, add_table
from data_query import add_row
#from create_table import drop_table, array_to_db

sheets = {}
#program setup

mycursor,mydb = database.get_cursor_db()

DEMO_ARRAY = [['name', 'age', 'hobby']
            ,['pepe', 'null', 'eat/sleep']
            ,['DIDI', '20', 'oh/yeah~']
            ,['6OOd', '1,2/', 'plAY/ball']
            ,['Good8man9', '3thirty3 three', 'scratch1ing head/and nose']
            ,['Good8man9', '3thirty3 three', 'scratch1ing head/and nose']
            ,['DIDI', '20', 'oh/yeah~']
			,['Object', 'null', 'NULL/null']]

NEW_ROW = {'name':'TEST1', 'age':'TEST2', 'hobby':'TEST3'}

add_table('myguy', DEMO_ARRAY, sheets, mycursor, mydb)
#duplicate_eliminate('myguy')
#remove_punctuation('myguy', 1, 2)
#remove_number('myguy', -1, 3)
#split_column_by('myguy','first', 'second', '/',  'hobby')
#print(sheets['myguy'])
#commit_change('myguy', sheets['myguy'], mycursor, mydb)
user_input = ""
while user_input != 'quit':
    user_input = input("user action:")
    table = input("choose table:")
    if not (table in list(sheets.keys())):
        print('reset. Please choose a existing table')
        continue
    if user_input == 'remove duplicate':
        remove_duplicate_input(sheets[table])
    elif user_input == 'change column name':
        change_c_name_input(sheets[table])
    elif user_input == 'split column':
        split_column_by_input(sheets[table])
    elif user_input == 'lower case':
        lower_case_input(sheets[table])
    elif user_input == 'upper case':
        upper_case_input(sheets[table])
    elif user_input == 'remove number':
        remove_number_input(sheets[table])
    elif user_input == 'merge column':
        merge_column_input(sheets[table])
    elif user_input == 'remove punctuation':
        remove_punctuation_input(sheets[table])
    elif user_input == 'replace value':
        replace_value_input(sheets[table])
    elif user_input == 'strip':
        strip(sheets[table])
    elif user_input == 'add test row':
        add_row(sheets['myguy'], NEW_ROW)
    elif user_input == 'pop row':
        pop_row_input(sheets[table])
    elif user_input == 'query all':
        print(sheets[table])
    elif user_input == 'search row':
        print(search_rows_input(sheets[table]))
    elif user_input == 'get column':
        print(get_col_input(sheets[table]))
    elif user_input == 'assignment2':
        print(get_assignment2_input(mycursor))
        # example:myguy.age: NOT null
    else:
        print('pleaze choose a valid action')
        continue
    commit_change(table, sheets[table], mycursor, mydb)
