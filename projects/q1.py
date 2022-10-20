# What is the average speed (Spd) of all Digimon? 
# literally pasted the code from penguin lab here: 

import csv    
with open("./datasets/digimon.csv", "r") as f: 
    avg_speed = {'speeds': 0.0 , 'counter': 0.0 , 'avg_return': 0.0} 
    data = csv.reader(f) 
    next(data) 
    for row in data: 
        avg_speed['speeds'] += int(row[12]) 
        avg_speed['counter'] += 1 
        avg_speed['avg_return'] = avg_speed['speeds'] / avg_speed['counter'] 
print("The average speed (Spd) of all Digimon is" , avg_speed['avg_return']) 
# look up way to format floats to a specific decimal point 


