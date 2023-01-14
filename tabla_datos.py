import statistics
import csv
from collections import Counter
from random import uniform

def demandTable(fileName, simulationTimes):
    file = open(fileName, newline='')
    reader = csv.reader(file, delimiter=',')
    valuesList = list()

    for row in reader:
        value = valuesToNumeric(row)
        valuesList.append(value)

    for values in valuesList:
        frecuency = getFrecuency(values)
        absoluteFrecuency = getAbsoluteFrecuency(frecuency)
        simulateFrecuency(absoluteFrecuency, simulationTimes)

    return valuesList	

def getFrecuency(values):
    values.sort()
    valuesCount = Counter(values)
    print(values)
    frequencyDict = dict()
    lenght = len(values)
    for key, value in valuesCount.items():
        frequencyDict[key] = value / lenght
    print('Frecuencia:' + str(frequencyDict))
    return frequencyDict

def getAbsoluteFrecuency(frequencyDict):
    totalSum = 0
    absoluteFrecencyDict = dict()
    for key, value in frequencyDict.items():
        totalSum += value
        absoluteFrecencyDict[key] = totalSum
        
    print('Frecuencia absoluta:' + str(absoluteFrecencyDict))
    return absoluteFrecencyDict

def simulateFrecuency(absoluteFrecuencyDict, simulationTimes):
    for simulation in range(simulationTimes):
        r = round(uniform(0, 1), 2)
        asociatedValue = 0
        asociatedFound = False
        for key, value in absoluteFrecuencyDict.items(): 
            if (value >= r and asociatedFound == False):
                asociatedFound = True
                asociatedValue = key
        print('R:' + str(r) + ', Valor: ' + str(asociatedValue))

		
def valuesToNumeric(values):
	newValues = list()
	for value in values:
		try:
			newValues.append(float(value))
		except:
			if value != '': newValues.append(value)
	return newValues

if __name__ := '__main__':
	fileName = 'datos_tabla.csv'
	demandTable(fileName, 10)