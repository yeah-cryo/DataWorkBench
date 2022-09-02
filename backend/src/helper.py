'''helper.py helps assembling frequently used functions from other files into one function'''

from create_table import drop_table, array_to_db

def commit_change(name, data, cursor, mydb):
    '''
    commit the change from backend into the database.
        Parameters:
                data (list): the data to be modified.
                name (str): the table name.
                cursor (database cursor): used to modify database.
                mydb (database object): use to commit change in database.
    '''
    drop_table(name, cursor)
    array_to_db(name, data[1:][:], data[0], cursor, mydb)

def add_table(name, data, sheet, cursor, mydb):
    '''
    add new table into the database.
        Parameters:
                data (list): the data to be modified.
                name (str): the table name.
                cursor (database cursor): used to modify database.
                mydb (database object): use to commit change in database.
                sheet (dicitonary): the local storage of the datasets.
    '''
    try:
        drop_table(name, cursor)
    except(Exception):
        print('table is not in db')
    sheet[name] = data
    if (len(data) == 1):
        array_to_db(name, [], data[0], cursor, mydb)
    else:
        array_to_db(name, data[1:][:], data[0], cursor, mydb)
