"""create_table.py contains functions to deleteor create a database table"""
import numpy as np

def drop_table(table_name, cur):
    '''
    drop a table from the database.
        Parameters:
                table_name (str): the name of the table to be modified.
                cur (database cursor): used to call the sql command line.
    '''
    # drop mysql table
    drop = 'DROP TABLE %s;' % table_name
    cur.execute(drop)

def array_to_db(table_name, data_in, field_in, cursor, mydb):
    '''
    convert a python array into a database table.
        Parameters:
                table_name (str): the name of the table to be modified.
                data_in (list): the 2d data array.
                field_in (list): a list of column name.
                cursor (database cursor): used to call the sql command line.
                mydb (the database object): used to commit changes in the database.
        return:
                invalid_input (str): error message.
    '''
    invalid_input = "Invalid input data"
    try:
        #check if data_in and field_in are iterable
        np.array(data_in)
        field = np.array(field_in)
        field_length = len(field)
    except Exception:
        print(invalid_input)

   # number of columns in current table
    column_query = ''
    #iterating fieldtable_names
    for index, i in enumerate(field):
        if i == '':
            break
        if index == field_length - 1:
            column_query += '%s VARCHAR(255)' % i
        else:
            column_query += '%s VARCHAR(255), ' % i
    query = 'CREATE TABLE IF NOT EXISTS %s (%s);' % (table_name, column_query)
    try:
        cursor.execute(query)
    except(Exception):
        print('invalid table name')
    # https://dev.mysql.com/doc/refman/8.0/en/create-table.html
    #inserting each row
    for record in data_in:
        ins = 'INSERT INTO %s\nValues (' % table_name
        for pindex, value in enumerate(record):
            if pindex == field_length - 1:
                if str(value) == '':
                    ins = ins + '""'
                else:
                    ins = ins + '"' + str(value) + '"'
                break
            if str(value) == '':
                ins = ins + '""' + ', '

            else:
                ins = ins + '"' +str(value)+ '"' + ', '
        ins = ins + ');'
        cursor.execute(ins)
    mydb.commit()
