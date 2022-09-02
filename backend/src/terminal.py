'''terminal.py contains functions used for displaying terminal interface'''

import data_cleaning
import data_query

def get_str(line):
    '''
    get a user input as string.
        Parameters:
                line (str): terminal interface prompt.
        return:
                user_input (str): the user input.
    '''
    user_input = ''
    while user_input == '':
        user_input = input(line)
    return user_input

def get_num(line):
    '''
    get a user input as int.
        Parameters:
                line (str): terminal interface prompt.
        return:
                user_input (int): the user input.
    '''
    user_input = -2
    while user_input == -2:
        try:
            user_input = int(input(line))
        except:
            print('please enter a integer >= 0')
            user_input = -2
    return user_input



def remove_duplicate_input(data):
    '''
    remove duplicate interface.
        Parameters:
                data (list): the data to be modified.
    '''
    data_cleaning.duplicate_eliminate_b(data)

def remove_punctuation_input(data):
    '''
    remove punctuation interface.
        Parameters:
                data (list): the data to be modified.
    '''
    column_num = get_num('column index:')
    row_num = get_num('row index:')
    data_cleaning.remove_punctuation_b(data, column_num, row_num)

def merge_column_input(data):
    '''
    merge column interface.
        Parameters:
                data (list): the data to be modified.
    '''
    col1 = get_str('name of first column:')
    col2 = get_str('name of second column:')
    spliter = get_str('spliter:')
    new_col = get_str('name of the new column:')
    data_cleaning.merge_column_b(col1, col2, spliter, data, new_col)

def remove_number_input(data):
    '''
    remove_number interface.
        Parameters:
                data (list): the data to be modified.
    '''
    column_num = get_num('column index:')
    row_num = get_num('row index:')
    data_cleaning.remove_number_b(data, column_num, row_num)

def upper_case_input(data):
    '''
    uppercase interface.
        Parameters:
                data (list): the data to be modified.
    '''
    column_num = get_num('column index:')
    row_num = get_num('row index:')
    data_cleaning.upper_case_b(data, column_num, row_num)

def lower_case_input(data):
    '''
    lowercase interface.
        Parameters:
                data (list): the data to be modified.
    '''
    column_num = get_num('column index:')
    row_num = get_num('row index:')
    data_cleaning.lower_case_b(data, column_num, row_num)

def split_column_by_input(data):
    '''
    split column interface.
        Parameters:
                data (list): the data to be modified.
    '''
    col1 = get_str('name of first new column:')
    col2 = get_str('name of second new column:')
    spliter = get_str('spliter:')
    new_col = get_str('name of the column:')
    data_cleaning.split_column_by_b(data,col1, col2, spliter,  new_col)

def change_c_name_input(data):
    '''
    change column name interface.
        Parameters:
                data (list): the data to be modified.
    '''
    old_name = get_str('old column name:')
    new_name = get_str('new column name:')
    data_cleaning.change_c_name_b(data, old_name, new_name)

def replace_value_input(data):
    '''
    replace_value interface.
        Parameters:
                data (list): the data to be modified.
    '''
    old_val = get_str('value to be replaced:')
    new_val = get_str('value to replace:')
    data_cleaning.replace_value_b(data, old_val, new_val)

def pop_row_input(data):
    '''
    pop_row interface.
        Parameters:
                data (list): the data to be modified.
    '''
    attr = get_str('from which column?:')
    val = get_str('what value?:')
    data_query.pop_row(data, attr, val)

def search_rows_input(data):
    '''
    search_rows name interface.
        Parameters:
                data (list): the data to be modified.
        return:
                list of rows.
    '''
    attr = get_str('from which column?:')
    val = get_str('what value?:')
    return data_query.search_rows(data, attr, val)

def strip(data):
    '''
    search_rows name interface.
        Parameters:
                data (list): the data to be modified.
        return:
                list of rows.
    '''
    attr = get_str('strip which?:')
    for i in data[1:]:
        for index, element in enumerate(i):
            i[index] = element.strip(attr)

def get_col_input(data):
    '''
    get column name interface.
        Parameters:
                data (list): the data to be modified.
        return:
                the column list
    '''
    attr = get_str('which column?:')
    return data_query.get_col(data, attr)

def get_assignment2_input(cursor):
    '''
    get query result using query language from assignment 2.
        Parameters:
                cursor (str): used to modify the database.
        return:
                The query result.
    '''
    query_line = get_str('query line:')
    return data_query.query_assignment2(query_line, cursor)