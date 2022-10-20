"""
You can access the Python shell by running python3 in your terminal!
I also recommend making a sandbox.py to test and check your answers.

1. How do you initialize a variable in Python?
Variables are initialized in Python the moment that a value is assinged to it. There is no need to initialize a varible by s
"var" --> simply write naomi = 1 (the value of naomi is 1). When creating a variable --> you're assigning a "number" of memory (allocating memory)


2. How does Python distinguish between different variable types?
Python deos not literally distinguish between variable types (cannot tell difference between variables and constants). If a variable
value has quotes around it, then Python will distinguish this variable as a string. If a value has a decimal, then Python will read this as
a float, and if is a number without a decimal point, Python will read this as a integer. 

3. Does Python check variable types statically or dynamically?
Python checks variables dynamically: the variable type is recognized by Python automatically, meaning the variable 
type does not have to be defined when the variable is defined.  (Variable types determined automatically during runtime). In general, static
typing requires less time devoted to memory allocation. 

4. What happens if you run a Python script and there is a bug?
When there is a Python script and there is a bug, the program does not run; the IDE tells the programmer in which line
the bug was found. There are different "classes" of errors (ex: syntax error/NameError/ValueError). 

5. Convert the following snippet into one line:
if (a and not b):
return False
else:
return True
"""
## Answer: 
#False if (a and not b) else True --> ternary operator  // return (not a or b) (this is returning the boolean value)

"""
6. Explain the difference between range(1,10) and range(1,10,2) .
For range(1,10) the program will return values/numbers for each index, 1-9 (ending value is not included). In terms of range(1,10,2)
the return will be the values/numbers at indexes 1-9, going up by twos. (can have steps or start or stop values be negative). Range function 
returns a range option (returns a list/array). Range itself 

7. Convert the following for-loop into a while-loop:
for i in range(2, 20, 3):
print(i)

Answer: 
""" 
while i in range(2,20,3):
    print(i)


""""
Write the following functions.


8. add(x,y) returns the sum of x and y
"""

def add(x,y):
    return x + y

""""
9. larger(x,y) returns the larger number

"""
def larger(x,y):
    print(x) if (x>y) else print(y)
"""

10. xor(a,b) returns whether exactly one input is True
"""
def xor(a,b):
    if (not(a == b)):
        return True 
    else:
         return False 
""""


11. hello(n) prints "hello" n times

""" 
def hello(n): 
    while n>0:
        print("hello")
        n -= 1 

""" 
12. fraction(n) prints the float representations of 1/2, 1/3, 1/4 ... 1/n

"""
def fraction(n):
   print(1/(n))


fraction(6)

""" 

13. factorial(n) returns the factorial of n (written as n! )
""" 

def factorial(n): 
    if n == (0):
        return(1)
    if n ==(1):
        return(n)  
    else:
        return(n * factorial(n-1)) 

print(factorial(0)) 

"""

14. stars(n) prints a right triangle of stars with height and base n 
ex: stars(3) should print:
*
**
***

 """ 

def stars(n):
    for i in range (1, n + 1):
            print ("*" * i)

stars (5)
