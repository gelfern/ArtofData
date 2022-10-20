""" 
1. Examine the following lists:
only in python (not java or scala) can you have a list with multiple data types 
digits = [0,1,2,3,4,5,6,7,8,9]
title = ["A", "Hundred", "Ghosts", "Parade", "Tonight"]
story = ["A Hundred Ghosts Parade Tonight", "Xia Jia", 2012]

i. How many elements does the list named contain?

digits: 10 
title: 5
story: 3

ii. What type of data is stored in each list?

digits:integers 
title: strings 
story: strings, integer


2. How would you define a list?
Type and enter the following Python code:

book = ["Minor","Feelings","by","Cathy", "Park", "Hong"]
print(book[0])

3. What is printed for book[0]?
"Minor"

4. What value in the list does book[3] represent?
"by"

5. Write a line of code that prints the last value.
print(book[5])

6. What happens if you try to print book[6] ? Why?
Out of bounds error --> the number elements in this list is 5. 

7. What does book[-1] return?
This always will return the last element in the list --> in this case it will return Hong 

8. Explain how positive and negative indexes locate specific elements.
Positive indexes start at zero and move up through the list. Negative indexes starting with -1 start with the final element of the list and as the 
negative number gets "bigger" (really, smaller), it returns the element that number of elements away from the starting element of the list. 

9. What is printed with this statement: print(book) ? How is the information displayed?
The entire list is displayed. It prints out the list exactly how it was created, including the brackets. ['Minor', 'Feelings', 'by', 'Cathy', 'Park', 'Hong']


""" 
book = ["Minor","Feelings","by","Cathy", "Park", "Hong"]
print(book) 

""" 

10. A veterinarian stores the names of each pet they examine.

pets = ["Apollo", "Bandit", "Nova", "Ginger",
"Mochi", "Honey", "Buster", "Arthur", "Taro"]

i. Examine the following code. What is being stored in for each iteration of the loop?
for pet in pets:
    print(pet)

Each element of the list, pets, is being stored in pet starting with the element at the [0] index. 

ii. Does anything change if we change to foo?
Nothing 

Model B | Insertion and Deletion
An athlete keeps track of how many minutes it takes for them to run a mile.

minute_miles = [8.4, 9.2, 8.1, 6.5, 6.1, 5.9, 7.4, 8.3, 6.2]

1. Explain what this code of line would do: minute_miles.append(7.3) 
It would add the number 7.3 to the end of the list. 

2. Write a line of code that would add 6.7 to the list.

minute_miles.append(6.7) 

3. What does minute_miles.insert(2, 8.8) do?
The number 8.8 is inserted into the list at the 2nd index. 

4. Write a line of code that would place 6.0 at the beginning of the list.
minute_miles.insert(0, 6.0)

5. Explain what this line of code would do: del minute_miles(2)
Would delete the number from the list at the second index. 

6. Write a line of code that would delete the last record in the list.
del minute_miles(-1) or also del minute_miles(8)

7. Explain what this line of code would do: minute_miles.remove(8.1) 
This specifically removes 8.1 from the list. The remove() function removes the first matching value from the list. 
The del() function is used to delete an element at a specified index number in the list.


8. Write a line of code that would delete 8.3 from the list.
minute_miles.remove(8.3) 

9. What would happen if the same time appears in the list twice, and remove() was used? Does that delete both?
No it doesnt delete both. It deletes the first instance. 

10. What happens if you try to remove 3.3?
Error because 3.3 isnt there. 
"""