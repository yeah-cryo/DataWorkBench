"""the unit test cases"""

import unittest
import data_cleaning
import data_query
import query_parser

class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.test_array = [['name', 'age', 'hobby']
                        ,['pepe', 'null', 'eat/sleep']
                        ,['DIDI', '20', 'oh/yeah~']
                        ,['6OOd', '1,2/', 'plAY/ball']
                        ,['Good8man9', '3thirty3 three', 'scratch1ing head/and nose']
                        ,['Good8man9', '3thirty3 three', 'scratch1ing head/and nose']
                        ,['DIDI', '20', 'oh/yeah~']
                        ,['Object', 'null', 'NULL/null']]

    def test_change_c_name(self):
        '''
        testing change_c_name()
            Parameters:
                    self (TestStringMethods): the self reference class varible.
        '''
        data_cleaning.change_c_name_b(self.test_array, 'age', 'test')
        self.assertEqual(self.test_array[0][1], 'test', 'change column name does nots work')

    def test_replace_value(self):
        '''
        testing replace_value()
            Parameters:
                    self (TestStringMethods): the self reference class varible.
        '''
        data_cleaning.replace_value_b(self.test_array, 'null', 'test')
        self.assertEqual(self.test_array[1][1], 'test', 'replace_value() does not work')
        self.assertEqual(self.test_array[7][1], 'test', 'replace_value() does not work')

    def test_duplicate_eliminate(self):
        '''
        testing duplicate_eliminate()
            Parameters:
                    self (TestStringMethods): the self reference class varible.
        '''
        data_cleaning.duplicate_eliminate_b(self.test_array)
        self.assertEqual(self.test_array[1][0], 'pepe', 'duplicate_eliminate() does not work')
        self.assertEqual(self.test_array[2][0], 'DIDI', 'duplicate_eliminate() does not work')
        self.assertEqual(self.test_array[3][0], '6OOd', 'duplicate_eliminate() does not work')
        self.assertEqual(self.test_array[4][0], 'Good8man9', 'duplicate_eliminate() does not work')
        self.assertEqual(self.test_array[5][0], 'Object', 'duplicate_eliminate() does not work')

    def test_split_column_by(self):
        '''
        testing split_column_by()
            Parameters:
                    self (TestStringMethods): the self reference class varible.
        '''
        data_cleaning.split_column_by_b(self.test_array, 'test1', 'test2', '/', 'hobby')
        self.assertEqual(len(self.test_array[0]), 4, 'split_column_by() does not work')
        self.assertEqual(self.test_array[0][2], 'test1', 'split_column_by() does not work')
        self.assertEqual(self.test_array[0][3], 'test2', 'split_column_by() does not work')

    def test_upper_case(self):
        '''
        testing upper_case()
            Parameters:
                    self (TestStringMethods): the self reference class varible.
        '''
        data_cleaning.upper_case_b(self.test_array, 0, 0)
        self.assertEqual(self.test_array[1][0], 'PEPE', 'upper_case() does not work')

    def test_lower_case(self):
        '''
        testing lower_case()
            Parameters:
                    self (TestStringMethods): the self reference class varible.
        '''
        data_cleaning.lower_case_b(self.test_array, 0, 1)
        self.assertEqual(self.test_array[2][0], 'didi', 'lower_case() does not work')

    def test_remove_number(self):
        '''
        testing remove_number()
            Parameters:
                    self (TestStringMethods): the self reference class varible.
        '''
        data_cleaning.remove_number_b(self.test_array, 0, 3)
        self.assertEqual(self.test_array[4][0], 'Goodman', 'remove_number() does not work')

    def test_replace_certain_character(self):
        '''
        testing replace_certain_character_b()
            Parameters:
                    self (TestStringMethods): the self reference class varible.
        '''
        data_cleaning.replace_certain_character_b(self.test_array, 'e', 'a')
        self.assertEqual(self.test_array[1][0], 'papa', 'replace_certain_charater_b() does not work')
    
    def test_remove_certain_character(self):
        '''
        testing remove_certain_character_b()
            Parameters:
                    self (TestStringMethods): the self reference class varible.
        '''
        data_cleaning.remove_certain_character_b(self.test_array, 'e')
        self.assertEqual(self.test_array[1][0], 'pp', 'remvoe_certain_charater_b() does not work')

    def test_slicer_b(self):
        data = data_cleaning.slicer_b(self.test_array, (1,1), (3,2))
        self.assertEqual(data[0][0], 'age', 'slicer_b() does not work')
    
    def test_slicer_b_index_out_of_bound(self):
        data = data_cleaning.slicer_b(self.test_array, (123,1), (242345,2))
        self.assertEqual(data, [['age']], 'slicer_b() does not work')
    
    def test_merge_column(self):
        '''
        testing merge_column()
            Parameters:
                    self (TestStringMethods): the self reference class varible.
        '''
        data_cleaning.merge_column_b('age', 'hobby', ',', self.test_array, 'test')
        self.assertEqual(self.test_array[0][1], 'test', 'merge_column does not work')
        self.assertEqual(self.test_array[1][1], 'null,eat/sleep', 'merge_column does not work')
        self.assertEqual(self.test_array[2][1], '20,oh/yeah~', 'merge_column does not work')
        self.assertEqual(self.test_array[3][1], '1,2/,plAY/ball', 'merge_column does not work')

    def test_remove_punctuation(self):
        '''
        testing remove_punctuation()
            Parameters:
                    self (TestStringMethods): the self reference class varible.
        '''
        data_cleaning.remove_punctuation_b(self.test_array, 1, 2)
        self.assertEqual(self.test_array[3][1], '12', 'remove_punctuation does not work')

    def test_add_row(self):
        '''
        testing add_row()
            Parameters:
                    self (TestStringMethods): the self reference class varible.
        '''
        data_query.add_row(self.test_array, {'name':'test1', 'age':'test2', 'hobby':'test3'})
        self.assertEqual(self.test_array[8][0], 'test1', 'add_row() does not work')
        self.assertEqual(self.test_array[8][1], 'test2', 'add_row() does not work')
        self.assertEqual(self.test_array[8][2], 'test3', 'add_row() does not work')

    def test_pop_row(self):
        '''
        testing pop_row()
            Parameters:
                    self (TestStringMethods): the self reference class varible.
        '''
        data_query.pop_row(self.test_array, 'name', 'DIDI')
        self.assertEqual(len(self.test_array), 6, 'pop_row() does not work')
        self.assertEqual(self.test_array[2][0], '6OOd', 'pop_row() does not work')

    def test_search(self):
        '''
        testing search_rows()
            Parameters:
                    self (TestStringMethods): the self reference class varible.
        '''
        search_result = data_query.search_rows(self.test_array, 'name', 'Object')
        self.assertEqual(search_result[0][0], 'Object', 'search_row does not work')

    def test_get_col(self):
        '''
        testing get_col()
            Parameters:
                    self (TestStringMethods): the self reference class varible.
        '''
        search_result = data_query.get_col(self.test_array, 'name')
        for i, result in enumerate(search_result):
            self.assertEqual(result, self.test_array[i+1][0], 'get_col does not work')

    def test_assembler_helper(self):
        query, field = query_parser.assembler_helper("select * from student ", 'age', '<=', '19')
        self.assertEqual(query, 'select * from student CAST(age AS DECIMAL) <= 19', 'assembler_helper doesnot work')
        self.assertEqual(field, 'age','assembler_helper doesnot work')

    def test_querier(self):
        select, condition, table_first = query_parser.querier('myguy.name: NOT asd AND myguy.age: > 3500')
        self.assertEqual(select, 'SELECT * FROM myguy', 'querier does not work')
        self.assertEqual(condition, '''WHERE (NOT name LIKE "%asd%") AND (CAST(age AS DECIMAL) > 3500)''', 'querier does not work')
        self.assertEqual(table_first, 'myguy', 'querier does not work')

    def test_format_checker(self):
        table, field, query = query_parser.format_checker('myguy.name: NOT asd')
        self.assertEqual(table, 'myguy', 'format_checker does not work')
        self.assertEqual(field, 'name', 'format_checker does not work')
        self.assertEqual(query, 'name LIKE "% NOT asd%"', 'format_checker does not work')
if __name__ == '__main__':
    unittest.main()
