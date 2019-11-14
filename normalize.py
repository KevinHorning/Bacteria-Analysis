# takes training data .csv file as input, normalizes the resistivity values,
# then writes normalized values and their resistance class in another .csv file

import csv

with open('D:/Coding/Python/FundDataSci/Bacteria/trainingData.csv') as infile:
    # makes lists of resistance values and finds mins and maxs from input file
    reader = csv.reader(infile)
    names = []
    list1 = []
    list2 = []
    min1 = min2 = max1 = max2 = 0
    for row in reader:
        if (row[0] != 'ï»¿Image_name'):   # if not first row
            names.append(row[0])
            resistance1 = int(row[1])
            list1.append(resistance1)
            if resistance1 < min1:
                min1 = resistance1
            if resistance1 > max1:
                max1 = resistance1
            resistance2 = int(row[2])
            list2.append(resistance2)
            if resistance2 < min2:
                min2 = resistance2
            if resistance2 > max2:
                max2 = resistance2

    # makes lists of normalized resistivity values      
    normalized1 = []
    normalized2 = []
    l = len(list1)     
    for i in range(l):
        normalized1.append(round((list1[i] - min1)/(max1 - min1), 3))
        normalized2.append(round((list2[i] - min2)/(max2 - min2), 3))
        
    # finds thresholds for resistivity labels,
    # thresholds are values at 30% percentile of acsendent sorted list
    sorted1 = sorted(normalized1, reverse = True)
    sorted2 = sorted(normalized2, reverse = True)
    threshold1 = sorted1[int(l * .3)]
    threshold2 = sorted2[int(l * .3)]

    # makes lists of resistance labels for all bacteria
    labels1 = []
    labels2 = []
    for i in range(l):
        if normalized1[i] >= threshold1:
            labels1.append('Yes')
        else:
            labels1.append('No')
        if normalized2[i] >= threshold2:
            labels2.append('Yes')
        else:
            labels2.append('No')
   
# writes .csv file with normalized resitance values and labels    
with open('D:/Coding/Python/FundDataSci/Bacteria/newTrainingData.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)
    writer.writerow(['Image Name', 'Resistance1', 'Resistance2', 'Resistant To 1?', 'Resistant To 2?'])
    for i in range(l):
        writer.writerow([names[i], normalized1[i], normalized2[i], labels1[i], labels2[i]])  