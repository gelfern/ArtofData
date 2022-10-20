# The Palmer Penguins is a great dataset to work with; it is clean and clearly labeled.
# Import csv and open the csv file as f to read
import csv
with open("datasets/penguins.csv", "r") as f:
    # Making our dictionaries to collect our data for each question
    islandTable = {}
    billLenList = {}
    massList = {}
    # Creating a csv reader object named data and isolating the heading of that list of rows. This heading has the names of the data collected, i.e. island, mass, etc.
    data = csv.reader(f)
    head = next(data)
    # Iterating through our rows of data
    for row in data:
        # this code first adds all species to a list with their own nested dictionay. Then will check over if the island has already been
        # stated within that species row, if it has, it will add the new row value to the species.
        if row[0] not in islandTable:
            islandTable[row[0]] = {}
        if head[1] not in islandTable[row[0]]:
            islandTable[row[0]][head[1]] = {}
        if row[1] not in islandTable[row[0]][head[1]]:
            islandTable[row[0]][head[1]][row[1]] = 1
        else:
            islandTable[row[0]][head[1]][row[1]] += 1

        # Finding billLengthAverage

        # Seperates penguin species and creates keys in a dictionary where our data will be collected.
        # In this case, the total bill length of all penguins of the specific species, the amount of penguins, and the average value.
        if row[0] not in billLenList:
            billLenList[row[0]] = {'total_bl': 0.0,
                                   'count': 0, 'billLenAvg': 1.0}
        # Seperates penguin species and creates keys in a dictionary where our data will be collected.
        if row[2] not in billLenList[row[0]]:
            # If our row isn't a float and there is no data to be collected, we pass over it.
            if row[2] != '':
                # Now it iterates through our rows and assigns the bill length of each penguin as a float to our total length key, adding
                # onto it every time for each species.
                billLenList[row[0]]['total_bl'] += float(row[2])
                # Also adds one count everytime we pass by a penguin of that species
                billLenList[row[0]]['count'] += 1
        # Takes the total bill length collected and count of each species and divides the mass by the number of penguins to give us the average float.
        billLenList[row[0]]['billLenAvg'] = billLenList[row[0]]['total_bl'] / billLenList[row[0]]['count']

        # Finding Penguin Mass

        # Seperates penguin species and creates keys in a dictionary where our data will be collected.
        # In this case, the total mass of all penguins of the specific species, the amount of penguins, and the average value.
        if row[0] not in massList:
            massList[row[0]] = {'total_mass': 0.0, 'count': 0, 'massAvg': 1.0}
        # Now it iterates through our rows and assigns the mass of each penguin as a float to our total mass key, adding onto it every time.
        if row[5] not in massList[row[0]]:
            # If our row isn't a float and there is no data to be collected, we pass over it.
            if row[5] != '':
                massList[row[0]]['total_mass'] += float(row[5])
                # Also adds one count everytime we pass by a penguin of that species
                massList[row[0]]['count'] += 1
                # Takes the total mass collected and count of each species and divides the mass by the number of penguins to give us the average float.
        massList[row[0]]['massAvg'] = massList[row[0]]['total_mass'] / massList[row[0]]['count']


# 1. Which species of penguins has the longest bills (on average)?
print("The species with the longest bill length on average are the Chinstrap penguins with a bill length average of " +
      str(billLenList['Chinstrap']['billLenAvg']) + '.')
# 2. Which species of penguins is the most massive (on average)?
print("The most massive species of penguin is the Gentoo with an average mass of " +
      str(massList['Gentoo']['massAvg']) + '.')
# 3. How many Chinstrap penguins are on Dream island?
print("There are " + str(islandTable['Chinstrap']
      ['island']['Dream']) + ' penguins on Dream Island.')