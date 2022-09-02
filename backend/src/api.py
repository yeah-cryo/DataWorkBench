"""api.py runs the flask apis"""
import flask
import io
from flask import request
from flask_cors import CORS, cross_origin
import sys, traceback
from contextlib import redirect_stdout
from create_table import drop_table
import database
from terminal import *
from data_cleaning import *
from helper import commit_change, add_table
from data_query import add_row, pop_row

app = flask.Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
app.config["DEBUG"] = True
sheets = {}
mycursor,mydb = database.get_cursor_db()
#user prone transition functions
def add_sheet(name, field, dataset=[]):
    '''
    add a table to the database and backend.
        parameters:
                name (str): the table name
                field (list): a list of column names
                dataset (list): a double array representing the dataset.
    '''
    if dataset!=[] and len(field) != (len(dataset[0])):
        return "length of dataset doesn't match the length of field"
    dataset.insert(0,field)
    add_table(name, dataset, sheets, mycursor, mydb)

def commit(table_name):
    '''
    comment the change in the backend to database.
        parameters:
                table_name (str): the table name
    '''
    commit_change(table_name, sheets[table_name], mycursor, mydb)

def insert_row(table_name, dic):
    '''
    insert a row to certain table
        parameters:
                table_name (str): the table name
                dic (dictionary): the dictionary that represents one row.
    '''
    add_row(sheets[table_name], dic)

def delete_row(table_name, attr, value):
    '''
    delete a row in certain table
        parameters:
                table_name (str): the table name
                attr (str): column name
                value (str): value to be popped.
    '''
    pop_row(sheets[table_name], attr, value)

def delete_sheet(table_name):
    '''
    delete a table from the database and backend.
        parameters:
                table_name (str): the table name
    '''
    drop_table(table_name, mycursor)
    sheets.pop(table_name)

def remove_punctuation(table_name, column_num, row_num):
    '''
    remove punctuation of the data.
        Parameters:
                table_name (str): the name of the table to be modified.
                column_name (int): the column index.
    			row_num (int): the row index
    '''
    remove_punctuation_b(sheets[table_name], column_num, row_num)

def merge_column(column_name1, column_name2, spliter, table_name, newname):
    '''
    merge two column of the data.
        Parameters:
    			column_name1 (str): the first column to be merged
    			column_name2 (str): the second column to be merged
    			spliter (str): the spliter that splits the merge data
                table_name (str): the name of the table to be modified.
                newname (int): the new column name.
    '''
    merge_column_b(column_name1, column_name2, spliter, sheets[table_name], newname)
def remove_number(table_name, column_num, row_num):
    '''
    remove number of the data.
        Parameters:
                table_name (str): the name of the table to be modified.
                column_name (int): the column index.
    			row_num (int): the row index
    '''
    remove_number_b(sheets[table_name], column_num, row_num)

def upper_case(table_name, column_num, row_num):
    '''
    uppercase the data.
        Parameters:
                table_name (str): the name of the table to be modified.
                column_name (int): the column index.
    			row_num (int): the row index
    '''
    upper_case_b(sheets[table_name], column_num, row_num)

def lower_case(table_name, column_num, row_num):
    '''
    lowercase the data.
        Parameters:
                table_name (str): the name of the table to be modified.
                column_name (int): the column index.
    			row_num (int): the row index
    '''
    lower_case_b(sheets[table_name], column_num, row_num)

def split_column_by(table_name,column_name1, column_name2, spliter,  cname):
    '''
    split a column of the data into two.
        Parameters:
    			column_name1 (str): the first column to be merged
    			column_name2 (str): the second column to be merged
    			spliter (str): the spliter that splits the merge data
                table_name (str): the name of the table to be modified.
                newname (int): the new column name.
    '''
    split_column_by_b(sheets[table_name],column_name1, column_name2, spliter,  cname)

def change_c_name(table_name,old_cname, new_cname):
    '''
    uppercase the data.
        Parameters:
                table_name (str): the name of the table to be modified.
                old_cname (str): the old column name to be changed.
    			new_cname (str): the new column name.
    '''
    change_c_name_b(sheets[table_name],old_cname, new_cname)

def duplicate_eliminate(table_name):
    '''
    remove duplication of the dataset.
        Parameters:
                table_name (str): the name of the table to be modified.
    '''
    duplicate_eliminate_b(sheets[table_name])

def replace_value(table_name, old_val, new_val):
    '''
    replace certain value of the data.
        Parameters:
                table_name (str): the name of the table to be modified.
                old_val (str): the value to be replaced.
    			new_val (str): the value to replace.
    '''
    replace_value_b(sheets[table_name], old_val, new_val)

def run_text_as_code(loc):
    '''
    Runs the string as python code, also collects the stdout and stderr for outputting
        Parameters:
                loc (str): the local python code.
        return:
                the message as string from stdout or stderr.
    '''
    try:
        with io.StringIO() as buf, redirect_stdout(buf):
            exec(loc, globals())
            output = buf.getvalue()
        return [output, "success"]
    except Exception:
        exc_type, exc_value, exc_traceback = sys.exc_info()
        trace_back = traceback.extract_tb(exc_traceback)
        stack_trace = list()

        for trace in trace_back:
            stack_trace.append("File : %s , Line : %d, Func.Name : %s, Message : %s" % (trace[0], trace[1], trace[2], trace[3]))
        s = "Exception type : %s " % exc_type.__name__
        d = "Exception message : %s" %exc_value
        f = "Stack trace : %s" %stack_trace
        out = s + '\n' + d + '\n' + f
        return [out, "exception"]

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404
@app.errorhandler(415)
def invalid_data_type(e):
    return "<h1>415</h1><p>Invalid data Type, requiring JSON</p>", 415

@app.route('/scriptBox', methods=['POST'])
@cross_origin()
def getarray():
    try:
        data = request.get_json()['text']
    except(Exception):
        return invalid_data_type(415)
    message = run_text_as_code(data)
    #assume we want resultFromScript
    output = sheets
    return {'result':output, 'terminal':message}

app.run()
