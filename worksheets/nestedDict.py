# Application
# Write a Python file to analyze favorite_colors.csv and create a nested dictionary that contains the
# answers to the following questions:


# # 1. How many students in 9th grade put blue as their favorite color?

#
import csv     
with open("./datasets/favorite_colors.csv", "r") as f:
    data = csv.reader(f)
    table = {"Total" : {}}
    next(data) #The .next() method returns the current row and moves to the next row.
    for row in data: 
        if row[1] not in table ["Total"]:
            table["Total"][row[1]] = 1
        else:
            table["Total"][row[1]] += 1
        
        if row[0] not in table:
            table[row[0]] = {} #if the grade number (row[0]) is not in table, create a dictionary inside with key row[0]
        if row[1] not in table[row[0]]:
            table[row[0]][row[1]] = 1
        else: table[row[0]][row[1]] += 1



       
print(table)
    
    # studentNums = {"grade": {}}
    # data = csv.reader(f)
    # for row in data: 
    #     for k in row.keys():
    #         if k == '9':
    #             for v in row.values():
    #                 if v == 'blue':
    #                     studentNums['blue'] = i
    #                     {} += 1
    #         if k == 'yellow':
    #             studentNums['yellow'] = x
    #             x += 1
    # print(studentNums)
    


# 2. How many students in total put yellow as their favorite color?
