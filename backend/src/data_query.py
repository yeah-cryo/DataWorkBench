'''data_query.py is a collection of data querying functions'''

#table modification
from query_parser import querier

def add_row(data, dic):
    '''
    add a row/record to the data.
        Parameters:
                data (list): the data to be modified.
                dic (dictionary): a dictionary that represents one row.
    '''
    #field= []
    row = []
    for key in dic:
        #field.append(key)
        row.append(dic[key])
    #if (len(sheets[s_name]) == 0):
    #    sheets[s_name].append(field)
    data.append(row)

def pop_row(data, attr, value):
    '''
    pop a rows/records from the data.
        Parameters:
                data (list): the data to be modified.
                attr (str): pop from which column.
                value (str): pop which value.
    '''
    print(attr, value)
    if len(data) == 0:
        return []
    index_f = 0
    dev = []
    for count, atr in enumerate(data[0]):
        if atr == attr:
            index_f = count
    for i, row in enumerate(data[1:]):
        if row[index_f] == value:
            dev.append(i+1)
    for i in reversed(dev):
        print(data.pop(i))
#data querying

def search_rows(data, attr, value):
    '''
    search a rows/records from the data.
        Parameters:
                data (list): the data to be modified.
                attr (str): search from which column.
                value (str): search which value.
        return:
                develops (list) the search result
    '''
    develops = []
    if len(data) == 0:
        return []
    index_f = 0
    for count, atr in enumerate(data[0]):
        if atr == attr:
            index_f = count
    for row in data[1:]:
        if row[index_f] == value:
            develops.append(row)
    return develops

def get_col(data, col_name):
    '''
    get a column from the data.
        Parameters:
                data (list): the data to be modified.
                col_name (str): search from which column.
        return:
                develops (list) the search result
    '''
    index_f = 0
    develops = []
    if len(data) == 0:
        return []
    for i,name in enumerate(data[0]):
        if name == col_name:
            index_f = i
    for row in data[1:]:
        develops.append(row[index_f])
    return develops


def query_assignment2(query_line, mycursor):
    '''
    do a query using query language from assignment 2.
        Parameters:
                query (str): the query language from assignment 2.
                mycursor (database cursor): used to call sql language on the database.
        return:
                develops (list) the search result
    '''
    rt_tp = querier(query_line)
    command_line = rt_tp[0] + ' ' + rt_tp[1]
    print(command_line)
    results = []
    try:
        mycursor.execute(command_line)
        results = mycursor.fetchall()
    except Exception:
        return []
    file_data = []
    for cur_tuple in results:
        file_data.append(list(cur_tuple))
    return file_data
    