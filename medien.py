import csv
with open('SOCR-weightWeight.csv')as f:
    reader=csv.reader(f)
    fileData=list(reader)
    
    #to remove the index of given data we are using pop method
fileData.pop(0)
    #print(fileData)

weightData=[]
for i in range(len(fileData)):
    weight=fileData[i][2]
    weightData.append(weight)

weightData.sort()
n=len(weightData)
if n % 2 == 0   :
    medien1=float(weightData[n//2]) 
    medien2=float(weightData[n//2-1])
    finalMedien=(medien1+medien2)/2
else:
    finalMedien=int(weightData[n//2])
print(finalMedien)
   

        


    