#CO2
#CH4
#NOX
#O3
#COs
#HCOs 

import random
import numpy
from carbrands import carBrands, carTypes
from file import File

minCarsSold = 1000
maxCarsSold = 1000000
minCO2 = 80
maxCO2 = 250
minCH4 = 0.08
maxCH4 = 0.34
minNOX = 0.1
maxNOX = 0.6
minCO = 0.5
maxCO = 2
minKm = 80000
maxKm = 500000

dataCount = 10

#CO2        CH4     NOX     CO     AverageKilometers
def createRandomStats(count):
    list = []
    list.append(["Brand","Type","CarsSold", "CO2", "CH4", "NOX", "CO", "KM"])
    for i in range(count):
        sublist = [carBrands[random.randint(0,len(carBrands))-1],carTypes[random.randint(0,len(carTypes))-1],random.randint(minCarsSold,maxCarsSold),random.uniform(minCO2,maxCO2),random.uniform(minCH4,maxCH4),random.uniform(minNOX,maxNOX),random.uniform(minCO,maxCO),random.uniform(minKm,maxKm)]
        list.append(sublist)
    return list


def main():
    file = File("Data.csv")
    list = createRandomStats(dataCount)
    print(*list, sep = "\n")
    for i in range(len(list)): 
        for j in range(len(list[i])-1): 
            file.writeSingleValue(str(list[i][j]))
        file.writeRawString(str(list[i][len(list[i])-1]))
        file.newColumn()
    file.closeFile()
if __name__ == '__main__':
    main()