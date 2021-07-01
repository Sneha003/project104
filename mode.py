import csv
from collections import Counter
with open ('SOCR-weightWeight.csv', newline = '') as Hw : 
    reader = csv.reader(Hw)
    fileData = list(reader)

fileData.pop(0)

newList = []
for counter in range(len(fileData)) : 
    newRow = fileData[counter][2]
    newList.append(newRow)

# noOfRows = len(newList)

# use Counter method to get number of occurences
data = Counter(newList)
get_mode_range = {
                    "75-85":0,
                    "85-95":0,
                    "95-105":0,
                    "105-115":0,
                    "115-125":0,
                    "125-135":0,
                    "135-145":0,
                    "145-155":0,
                    "155-165":0,
                    "165-175":0,


}


for weight, occurence in data.items() : 
    weight = float(weight)
    if (75 < weight < 85) : 
        get_mode_range["75-85"] += occurence

    elif (85 < weight < 95) : 
        get_mode_range["85-95"] += occurence

    elif (95 < weight < 105) : 
        get_mode_range["95-105"] += occurence

    elif (115 < weight < 125) : 
        get_mode_range["115-125"] += occurence

    elif (125 < weight < 135) : 
        get_mode_range["125-135"] += occurence

    elif (135 < weight < 145) : 
        get_mode_range["135-145"] += occurence

    elif (145 < weight < 155) : 
        get_mode_range["145-155"] += occurence

    elif (155 < weight < 165) : 
        get_mode_range["155-165"] += occurence

    elif (165 < weight < 175) : 
        get_mode_range["165-175"] += occurence     

        



mode_range, mode_occurence = 0,0
for range, occurence in get_mode_range.items():
    if occurence > mode_occurence:
        mode_range,mode_occurence =  [int(range.split("-")[0]), int(range.split("-")[1])], occurence
mode = float((mode_range[0] + mode_range[1]) / 2)
print(f"The mode is {mode:2f}")


