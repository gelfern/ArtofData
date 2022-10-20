# Code for Reading File Practice (Naomi Gelfer)
# Collaborated with Nate Garelik in preliminary stages of coding (ideas/peer editing)
# Lengthier comments that describe lines are found under the lines they explain

import csv    
with open("./datasets/penguins.csv", "r") as f:
    #Initializing the dictionaries where data to answer each question will be stored 
    lengths = {}
    masses = {}
    peng_totals = {}
    
    data = csv.reader(f) #returns an iterable reader object of the csv file assigned to var data 
    next(data) #The .next() method returns the current row and moves to the next row.
    for row in data: #begin iterating through each row of data (csv reader object)

#CODE FOR QUESTION #1: Which species of penguins has the longest bills (on average)? 
# Create nested dictionaries as the values for three separate keys (each species of penguin)        
       
        if row[0] not in lengths: 
                lengths[row[0]] = {'total_lens': 0.0 , 'counter': 0.0 , 'avg_return': 0.0} 
                #creates a new key/value pair in the dictionary "lengths" --> its key is the penguin species and its value is
                #a nested dictionary that keeps track of a running total of the bill lengths for the species, 
                # a counter of the population of penguins in that species, 
                # and a placeholder value for the calculated average bill length of the species
                # (each is a separate k/v pair in the nested dictionary value of each species key)
        if row[2] not in lengths[row[0]] and row[2] != "": #confirms that the value of bill length in the for loop iteration is a float (not empty)
            lengths[row[0]]['total_lens'] += float(row[2]) 
            lengths[row[0]]['counter'] += 1 
            #Updates the running total bill lengths in a species by adding the bill length of the current instance of penguin to the total
            #and then adds one to the counter value for a species (since it just iterated through one penguin of a specific species)
        lengths[row[0]]['avg_return'] = lengths[row[0]]['total_lens'] / lengths[row[0]]['counter'] 
        #This line actually calculates the average bill length for a specific species and updates the value 
        #of key "avg_return' that is found within the nested dictionary value for each key species.  

#CODE FOR QUESTION #2: Which species of penguins is the most massive (on average)?
#The logic followed for this code is exactly the same as for Question 1, except now it updates the dictionary "masses" (instead of 
#"lengths") and calculates the total mass of each species (still counts total population of each species through the "counter" key). 
#Also, the value of "avg_return" in this code is the average mass of each species (not the bill length)

        if row[0] not in masses: 
            masses[row[0]] = {'total_mass': 0.0 , 'counter': 0.0 , 'avg_return': 0.0}
        if row[5] not in masses[row[0]] and row[2] != "": 
            masses[row[0]]['total_mass'] += float(row[5])
            masses[row[0]]['counter'] += 1 
        masses[row[0]]['avg_return'] = masses[row[0]]['total_mass'] / masses[row[0]]['counter']


#CODE FOR QUESTION #3: How many Chinstrap penguins are on Dream island?  
#Ultimately creates a nested dictionary as the value for each key species --> each nested dictionary contains key-value pairs 
#that denote each island a specific species can be found on (key) and how many penguins in that species live on it (value) 
       
        if row[0] not in peng_totals:
            peng_totals[row[0]] = {} #Create a new dictionary value inside of dictionary "peng_totals" with key species name
        if row[1] not in peng_totals[row[0]]: 
            peng_totals[row[0]][row[1]] = 1 #Sets up counter key-value pairs inside of each nested dictionary 
             # --> key = island name | value = count of total penguins (starting at 1)
        else: peng_totals[row[0]][row[1]] += 1 #If the island name key already exists 
            #in the nested dicitonary value for a speciic species, 
            # --> add one to the counter value for that island in that species 


# PRINT STATMENTS (output of each print statement is the answer to each of the three questions )
# For loops were created to answer the first two questions --> iterate through the dictionaries (lengths and masses) to 
# find the greatest average bill length and mass betweeen the three species, respectively. 

#Initialize vars that will store the greatest value of bill length avg or mass avg and the penguin species that "greatest" relates to
greatest = 0
peng_name = ""

for key in lengths: #"Key in lengths is each species name" --> iterate through lengths by species name 
                    #(values of each key are nested dictionaries, with one key inside of these dictionaries being the average bill length for that species)
            if lengths[key]['avg_return'] > greatest: 
                greatest = lengths[key]['avg_return'] 
                peng_name = key 
                #If the value of the average bill length of the species at the current iteration of the for loop is greater 
                #than the current value of "greatest," replace the value of "greatest" with that average bill length
                #and replace peng_name with the name of that penguin species (which corresponds to the new value of "greatest"). 
print("The" , peng_name , "species has the longest bill length, averaging at" ,greatest ,"mm.")   

#The following loop for question 2 follows same logic as in the for-loop for question 1 to find the penguin species with the greatest average mass. 
for key in masses: 
    if masses[key]['avg_return'] > greatest: 
        greatest = masses[key]['avg_return'] 
        peng_name = key 
print("The" , peng_name , "species is the most massive, averaging at" ,greatest , "g.")  


print("There are" , peng_totals['Chinstrap']['Dream'] , "Chinstrap penguins on Dream island.") 
#accessing the specific value of Chinstrap penguins on Dream island


#Notes for future self: 
# I would like to find a way to consolidate my answers to the first two questions into one dictionary 
# instead of two separate dictionaries (lengths and masses). Also, it would be fun to make this program
# "user-friendly" --> take inputs instead of having predetermined print statements to answer specific questions 
# --> i.e. the user asks how many Gentoo penguins are on Biscoe island and the program returns a specific answer