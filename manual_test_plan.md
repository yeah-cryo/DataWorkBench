# Manual test plan
- [1.Introducation](#1introducation)
- [2.Environment Setup](#2environment-setup)
- [3.unittest cases](#3unittest-cases)
- [4.Data editing methods](#4data-editing-methods)
    + [4.1.data cleaning functions](#41data-cleaning-functions)
    + [4.2.data querying functions](#42data-querying-functions)
- [5.database importing method](#5database-importing-method)
- [6.Manual testing strategy](#6manual-testing-strategy)
- [7. Backend Test cases](#7-backend-test-cases)
    + [7.1 @test verifying de-duplication](#71--test-verifying-de-duplication)
    + [7.2 @test verifying replace value](#72--test-verifying-replace-value)
    + [7.3 @test verifying  change column name](#73--test-verifying--change-column-name)
    + [7.4 @test verifying split_column_by](#74--test-verifying-split-column-by)
    + [7.5 @test verifying lower_case_b](#75--test-verifying-lower-case-b)
    + [7.6 @test verifying upper_case_b](#76--test-verifying-upper-case-b)
    + [7.7 @test verifying remove_number_b](#77--test-verifying-remove-number-b)
    + [7.8 @test verifying merge_column_b](#78--test-verifying-merge-column-b)
    + [7.9 @test verifying remove_punctuation_b](#79--test-verifying-remove-punctuation-b)
    + [7.10 @test verifying add_row](#710--test-verifying-add-row)
    + [7.11 @test pop_row](#711--test-pop-row)



## 1.Introducation
The program under test is a data workbench on sql/csv. The data modification happens in the backend and can be commited into mysql database by the commit function.

## 2.Environment Setup
* Python 3.9.5
* pip install : dotenv, pylint.
* Vscode with Python 3.9.5 64-bit extension
* windows 10

## 3.unittest cases
there is a unittest case in the program file that verifies the functionality of helper function.
To do the unit testing, run the unit_test.py in the path backend/src .

## 4.Data editing methods
There various data editing method which can be separated into two categories -- data query and data cleaning.

#### 4.1.data cleaning functions
* remove_punctuation_b(data, c_num, r_num) # remove punctuation from the data
* merge_column_b(c1, c2, spliter, data, newname) # merge two columns
* remove_number_b(data, c_num, r_num) # remove number from the data
* upper_case_b(data, c_num, r_num) # upper case alphabetic characters.
* lower_case_b(data, c_num, r_num) # lower case alphabetic characters.
* split_column_by_b(data,c1, c2, spliter,  cname) # split one column into two
* change_c_name_b(data,cname, new_cname) # change a column's name
* replace_value_b(data, old_val, new_val) # replace a some values with a new value.
* duplicate_eliminate_b(data) # eliminate duplication in the dataset

#### 4.2.data querying functions
* add_row(data, dic) # add a new row into the dataset
* pop_row(data, attr, value) # remove certain rows from the dataset
* search_rows(data, attr, value) # finding some rows in the dataset
* get_col(data, col_name) # get a column as a list
* query_assignment2(query_line, mycursor) # query the dataset using query language from assignment2

## 5.database importing method

This program imports data into the mysql database by using the library mysql.connector.
mysql.connector can be taken as a medium for communication between the scraping program and the mysql database.
After setting the server user and password correctly, we can use the sql cursor from cursor() to manipulate the content of database.

## 6.Manual testing strategy
Although unit testing tests some of the functions' functionality, We still need to check if the result of the commit is propagated into the database.



## 7. Backend Test cases

#### 7.1 @test verifying de-duplication 
After calling the duplication_elimination(), we can verify the result by using the sql 'count' by checking if some previously duplicated records are reduced to one.

#### 7.2 @test verifying replace value
We can check if certain value is replaced by setting the condition to this value, in sql 'where field = the value'. we can verify by checking if the result is empty.
#### 7.3 @test verifying  change column name
We can verify this by select the new column name.

#### 7.4 @test verifying split_column_by
We can verify this by select the two new column names and the old column, the result of selecting old column name should be empty.

#### 7.5 @test verifying lower_case_b
we can verify this by querying data we just lower-cased and check if they are lower-cased.

#### 7.6 @test verifying upper_case_b
we can verify this by querying data we just upper-cased and check if they are upper-cased.
#### 7.7 @test verifying remove_number_b
we can verify this by querying data we just modified and check if they contain any number.

#### 7.8 @test verifying merge_column_b
We can verify this by select the two old column names and the new column, the result of selecting old column names should be empty.

#### 7.9 @test verifying remove_punctuation_b
we can verify this by querying data we just modified and check if they contain any punctuations.

#### 7.10 @test verifying add_row
we can verify this by querying the row we just added and check if the result matches our input.

#### 7.11 @test pop_row
we can verify this by querying the row we just poped and check if the result is empty.

## 8. Frontend test cases WEEK 2

#### 8.1 @test web UI
the UI of the app should look like this.
![](screenshots/appUI.png)
#### 8.2 @test writing in the code block
user should be able to write text in the code block.
#### 8.3 @test add code block
more code block can be added by clicking add code block.
![](screenshots/adding_code_block.png)
#### 8.4 @test submit python code
user can compile python code by clicking submit.
![](screenshots/submit_code.png)
#### 8.5 @test console standard out
the console at the bottom of the code block should be able to print message from standard out. we can test this by printing something.
![](screenshots/console_stdout.png)
#### 8.6 @test console error out
the console should be able to display the errors and indicates which block causes the error.
![](screenshots/console_err.png)

## 9. Frontend test cases WEEK 3

#### 9.1 @basic spreadsheet
User should see a spreadsheet like this after opening the page.
![](screenshots/spreadsheet.png)
#### 9.2 @test editing spreadsheet
User should be able to edit the spreadsheet directly by clicking on cell.
![](screenshots/editing_spreadsheet.png)

#### 9.3 @test modifying spreadsheet with code.
With correct python code, the compiling result should affect the spreadsheet on the left. for example, this image shows what happen if we add a table to the database.
![](screenshots/code_spreasheet.png)

#### 9.4 @test multiple spreadsheets
if there are multiple table in the database, there should be a navigator below the spreadsheet to navigate among sheets.
![](screenshots/Multiple_sheets.png)

#### 9.5 @test column header
the column name should appear in the first row.
![](screenshots/First_row_columns.png)

#### 9.6 @test scroll bar
user can scroll down the spreadsheet.
![](screenshots/scroll.png)