"""
Dictionaries
Examine and run the following code:

""" 
story = {
"title": "Invisible Planets",
"author": "Hao Jingfang",
"published": 2013
}

""" 
Access

. Describe what information the dictionary named story contains.
The title of the story (Invisible Planets), the author of the story, and the year it was published (2013 is an integer). 

. What does story['author'] return?
Hao Jingfang 

. How does Python know that "Hao Jingfang" is related to author? Where is that relationship defined?
Because right before it says "author:" 

. In the line story['author'], what does the value in the square brackets represent?
The value/string attributed to author. 

. Write a line of code to print the title of the story.
story['title']

. How would you describe the keys and values of this dictionary?



Mutation
. Run this code: story["words"] = 6359, and then print story. What changes?

""" 
story["words"] = 6359
print(story)
"""
. Run this code: story["title"] = "Folding Beijing". What changes?
. Describe what the assignment operator (=) does in the context of dictionaries.
. Write a line of code to add the key "translator" and value "Ken Liu" to story.
. Run this code: del story['published']. What happens?
. Write a line of code to change the value of a key "B48" to 15 in a dictionary named classrooms.
. Write a line of code to delete the entry with key "B48" in a dictionary named classrooms.
Iteration
. What gets printed in the following snippet of code?
for x in story:
print(x)
. What is a better name for the variable than x?
. How do we iterate through a dictionary's values?

. Explain what is happening in the following snippet of code. Some useful terms are tuple and unpacking.
for (k,v) in story: --> this code does not work --> too many things to unpack (need to iterate thru 
story.items to get tuples (immutable lists or smth) --> without story.items it would just iterate thru 
the dictionary and only print the keys )
    print(k)
    print(v)

Application
. Write a function count() that takes a list of strings as input and outputs a dictionary where each unique string
is a key, and its count is the value. For example, count(["hello", "hello", "world", "hello"])

""" 

for key in story:
    print(story[key])
# . Explain what is happening in the following snippet of code. Some useful terms are tuple and unpacking.
for key in story:
    print(key)
    print(story[key])



    
def count(str):
    test = {}
    n = 0
    for i in str:
        test[i] = str.count(i)
        n += 1
    print(test)


testDict = ["Hello", "Hello", "World"]

count(testDict)

        

""" 

should return {"hello": 3, "world": 1}

"""