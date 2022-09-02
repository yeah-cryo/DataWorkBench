"""data_cleaning.py is collection of data cleaning functions"""
import numpy as np
import string

def remove_punctuation_b(data, c_num, r_num):
    '''
    remove punctuation of the data.
        Parameters:
                data (list): the data to be modified.
                column_name (int): the column index.
				row_num (int): the row index
    '''
    if c_num == -1 and r_num > -1:
        for index, i in enumerate(data[r_num+1]):
            st = str(i)
            for j in st:
                if j in string.punctuation:
                    st = st.replace(j, '', 1)
            data[r_num+1][index] = st

    elif (r_num == -1 and c_num > -1):
        for i in data:
            st = str(i[c_num])
            for j in st:
                if j in string.punctuation:
                    st = st.replace(j, '', 1)
            i[c_num] = st

    elif (r_num >= -1 and c_num > -1):
        st = str(data[r_num+1][c_num])
        for j in st:
            if j in string.punctuation:
                st = st.replace(j, '', 1)
        data[r_num+1][c_num] = st

def merge_column_b(c1, c2, spliter, data, newname):
    '''
    merge two column of the data.
        Parameters:
				column_name1 (str): the first column to be merged
				column_name2 (str): the second column to be merged
				spliter (str): the spliter that splits the merge data
                data (list): the data to be modified.
                newname (int): the new column name.
    '''
    temp = data
    index1 = -1
    index2 = -1
    for j,i in enumerate(temp[0]):
        if i == c1:
            index1 = j
        elif i == c2:
            index2 = j
    if index1 != -1 and index2 != -1:
        temp[0][index1] = newname
        temp[0].pop(index2)
        for i,j in enumerate(temp[1:]):
            j[index1] = str(j[index1]) + spliter + str(j[index2])
            j.pop(index2)
    print("done")

def remove_number_b(data, c_num, r_num):
    '''
    remove number of the data.
        Parameters:
                data (list): the data to be modified.
                column_name (int): the column index.
				row_num (int): the row index
    '''
    if (c_num == -1 and r_num > -1):
        for index, i in enumerate(data[r_num+1]):
            st = str(i)
            result = ''.join([j for j in st if not j.isdigit()])
            data[r_num+1][index] = result
    elif (r_num == -1 and c_num > -1):
        for i in data:
            st = str(i[c_num])
            result = ''.join([j for j in st if not j.isdigit()])
            i[c_num] = result
    elif (r_num >= -1 and c_num > -1):
        st = str(data[r_num+1][c_num])
        result = ''.join([j for j in st if not j.isdigit()])
        data[r_num+1][c_num] = result

def upper_case_b(data, c_num, r_num):
    '''
    uppercase the data.
        Parameters:
                data (list): the name of the table to be modified.
                column_name (int): the column index.
				row_num (int): the row index
    '''
    if c_num == -1 and r_num > -1:
        for index, i in enumerate(data[r_num+1]):
            data[r_num+1][index] = str(i).upper()
    elif r_num == -1 and c_num > -1:
        for i in data:
            i[c_num] = str(i[c_num]).upper()
    elif r_num >= -1 and c_num > -1:
        data[r_num+1][c_num] = str(data[r_num+1][c_num]).upper()

def lower_case_b(data, c_num, r_num):
    '''
    lowercase the data.
        Parameters:
                data (list): the data to be modified.
                column_name (int): the column index.
				row_num (int): the row index
    '''
    if c_num == -1 and r_num > -1:
        for index, i in enumerate(data[r_num+1]):
            data[r_num+1][index] = str(i).lower()
    elif r_num == -1 and c_num > -1:
        for i in data:
            i[c_num] = str(i[c_num]).lower()
    elif r_num >= -1 and c_num > -1:
        data[r_num+1][c_num] = str(data[r_num+1][c_num]).lower()

def split_column_by_b(data,c1, c2, spliter,  cname):
    '''
    split a column of the data into two.
        Parameters:
				column_name1 (str): the first column to be merged
				column_name2 (str): the second column to be merged
				spliter (str): the spliter that splits the merge data
                data (list): the data to be modified.
                newname (int): the new column name.
    '''
    index = -1
    for j,i in enumerate(data[0]):
        if i == cname:
            index = j
            break
    if index != -1:
        data[0][index] = c1
        data[0].append(c2)
        for row in data[1:]:
            splits = row[index].split(spliter)
            row[index] = splits[0]
            if len(splits) > 1:
                row.append(splits[1])
            else:
                row.append('')

def remove_certain_character_b(data, char):
    '''
    remove certain character from the dataset.
        Parameters:
                data (list): the data to be modified.
                char (string): the character to be removed.
    '''
    for row in data[1:]:
        for index, ele in enumerate(row):
            row[index] = ele.replace(char, '')

def slicer_b(data, top_l, right_l):
    header = data[0]
    temp = data[1:]
    try:
        header = header[top_l[1]:right_l[1]]
        temp = temp[top_l[0]:right_l[0] + 1][top_l[1]:right_l[1]]
        temp = list(temp)
        header = list(header)
        temp.insert(0, header)
        return temp
    except:
        print('index out of bound')
        return []
        


def replace_certain_character_b(data, char, new_char):
    '''
    split a column of the data into two.
        Parameters:
                data (list): the data to be modified.
                char (string): the character to be replaced.
                new_char (string): the character to replace.
    '''
    for row in data[1:]:
        for index, ele in enumerate(row):
            row[index] = ele.replace(char, new_char)

def change_c_name_b(data,cname, new_cname):
    '''
    uppercase the data.
        Parameters:
                data (list): the data to be modified.
                old_cname (str): the old column name to be changed.
				new_cname (str): the new column name.
    '''
    temp = data
    for j,i in enumerate(temp[0]):
        if i == cname:
            temp[0][j] = new_cname
            break

def replace_value_b(data, old_val, new_val):
    '''
    replace certain value of the data.
        Parameters:
                data (list): the data to be modified.
                old_val (str): the value to be replaced.
				new_val (str): the value to replace.
    '''
    if len(data) == 0:
        return "invalid_input"
    for row in data[1:]:
        for index, i in enumerate(row):
            if i == old_val:
                row[index] = new_val

def duplicate_eliminate_b(data):
    '''
    remove duplication of the dataset.
        Parameters:
                data (list): the data to be modified.
    '''
    if len(data) == 0:
        return "invalid_input"
    index = 1
    while index < len(data):
        cur_data = data[index]
        index_to_pop = []
        for j in range(len(data))[index+1:]:
            to_compare = data[j]
            is_the_same = True
            for k in range(len(data[0])):
                if cur_data[k] != to_compare[k]:
                    is_the_same = False
                    break
            if is_the_same:
                index_to_pop.append(j)
        for i in reversed(index_to_pop):
            data.pop(i)
        index = index + 1
            