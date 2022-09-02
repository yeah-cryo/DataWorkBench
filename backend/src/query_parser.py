
def assembler_helper(query, field, sign, value):
    '''
    helper function of format_checker,assembler_helper assembles the sql command line for the query.
        Parameters:
                sign (str): the equivalence sign includes < > =.
                field (str): the field name of the database.
                value (str): the value of corresponding field.
                content (str): the rows that will be added into database.
        Returns:
                query (str): the updated query command line
                field (str): the field name, it's returned for error checking.
    '''
    try:
        int(value)
    except Exception:
        field = ''
    query = query + 'CAST(' + field + ' AS DECIMAL)' + ' ' + sign + ' ' + value
    return query, field

def format_checker(parse_line):
    '''
    format_checker converts the primitive query line into the sql query command line.
        Parameters:
                parse_line (str): the primitive query line come with the requesting url.
        Returns:
                table (str): the table to be queried
                field (str): the fields that are included in the query condition.
                query (str): the complete condition line of the whole command line.
    '''
    table = ''
    field = ''
    query = ''
    dot_spliter = parse_line.split('.') # split by '.'
    table = dot_spliter[0]
    if len(dot_spliter) > 1:
        colon_spliter = dot_spliter[1].split(':') # split by ':'
        field = colon_spliter[0]
        if len(colon_spliter) > 1:
            temp_query = colon_spliter[1]
            if temp_query[:3] == 'NOT':
                query = query + 'NOT '
                temp_query = temp_query[3:]
            unequal_sign = False
            sign = ''
            if temp_query[0] == '>' or temp_query[0] == '<': # check if < or > exist
                unequal_sign = True
                sign = temp_query[0]
                temp_query = temp_query[1:]
            if temp_query[0] == '"': # check if we have double quote
                value = '"'
                for index,i in enumerate(temp_query[1:]): # iterate through the condition (after : )
                    if i != '"':
                        if index != (len(temp_query[1:]) - 1):
                            if i == '*':
                                value = value + '%'
                            else:
                                value = value + i
                    if index == (len(temp_query[1:]) - 1) and i != '"':
                        table = ''
                        field = ''
                value = value + '"'
                if unequal_sign:
                    # unequal sign
                    query, field = assembler_helper(query, field, sign, value)
                else:
                    query = query + field + ' LIKE ' + value
            else:
                if unequal_sign:
                    # unequal sign
                    query, field = assembler_helper(query, field, sign, temp_query)
                else:
                    query = query + field + ' LIKE ' + '"%' + temp_query + '%"'
    return table, field, query

def querier(arg):
    '''
    querier divide a bigger query line into several small query line by spliting the bigger query line by AND or OR.
    Then querier feed the small query line into format_checker and assembles the results into a more completed query line.
        Parameters:
                arg (str): the Big primitive query line
        Returns:
                select (str): the sql command line prefix that determine which field and table into query.
                condition (str): the conditional sql command line suffix that work as filter of data.
                table_first (str): the table we are querying at.
    '''
    arg = arg.replace(" ", "")
    print(arg)
    args = [arg]
    mid_sign = ''
    if 'AND' in arg:
        args = arg.split('AND')
        mid_sign = 'AND'
    elif 'OR' in arg:
        args = arg.split('OR')
        mid_sign = 'OR'
    select = ''
    condition = "WHERE "
    table_first = ''
    for index,argument in enumerate(args):
        table, field, query = format_checker(argument)
        if (table == '' or field == '' or query == ''):
            return 'format_error', (table , field, query)
        if index == 0:
            table_first = table
            select = "SELECT " + '*' + " FROM " + table
            condition = condition + "(" + query + ")"
            if len(args) == 2:
                condition = condition + ' ' + mid_sign + ' '
        elif index == 1:
            if table != table_first:
                return 'format_error', (table , field, query)
            condition = condition + "(" + query + ")"
    return select, condition, table_first

#print(querier('myguy.name: NOT asd AND myguy.age: > 3500'))
