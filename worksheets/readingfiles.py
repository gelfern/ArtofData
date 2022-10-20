
import csv 
# Download favorite_colors.csv and put it in a folder named datasets in your Art of Data folder.
# Model A
# 1. What does csv stand for?
# Comma separated values

# 2. What information does favorite_colors.csv contain?
# It contains a student's grade and their favorite color. 

# Model B
# Examine and run the following snippet of code. 
##with open("datasets/favorite_colors.csv", "r") as f:
    ##print(f)

# 1. What is printed when you run this code? --> 
# <_io.TextIOWrapper name='datasets/favorite_colors.csv' mode='r' encoding='UTF-8'>

# 2. Explain the syntax of the open() function.
# used to open a file: In the parenthesis --> () --> (filename, mode) --> r is to read  

# 3. Explain what you would need to change if you wanted to write to the file.
# change "r" to "w"

# 4. Explain why open() is called inside a with statement. 
# The with statement closes the file for the user without having to write the close() function after the open() function
# 
# Model C
# Examine and run the following snippet of code.

with open("datasets/favorite_colors.csv", "r") as f:
    data = csv.reader(f) # make a reader object for the file object 
    for row in data:
        print(row)

# 1. What module is being imported? Link to the official documentation for this module.
#csv.reader is being imported. https://docs.python.org/3/library/csv.html 

# 2. What does csv.reader() return?
# Return a reader object which will iterate over lines in the given csvfile. 

# 3. What is printed when you run this code?
# The entire file, with each grade as a string (COMMA) the color in brackets. 

# 4. Explain how to interpret the for-loop and row in terms of the csv file.

# Model D
# Examine and run the following snippet of code.

# import csv
# with open("datasets/favorite_colors.csv", "r") as f:
#     data = csv.DictReader(f)
#     for row in data:
#         print(row)

# 1. What does csv.DictReader() return, and how is this different from csv.reader()?
# just .reader returns individual lists of each row's values
# dictReader returns individual dictionaries of each row the keys and value s


# 2. What is printed when you run this code?
# 3. Explain how to interpret the for-loop and row in terms of the csv file.
# Application
# Write a Python file to analyze favorite_colors.csv and create a nested dictionary that contains the
# answers to the following questions:


# # 1. How many students in 9th grade put blue as their favorite color?

 
with open("datasets/favorite_colors.csv", "r") as f:
    data = csv.reader(f)
    for row in data:
        print(row)

# 2. How many students in total put yellow as their favorite color?

