#!/usr/bin/env python3

from modelo_descriptiva_datos import ModeloDescriptivaDatos
import statistics
import csv

def descriptiva_datos(file):
	reader = csv.reader(file, delimiter=',')
	modelList = list()
	for row in reader:
		values = valuesToNumeric(row)
		modelo = ModeloDescriptivaDatos(values,
		 statistics.mean(values),
		 statistics.mode(values),
		 statistics.median(values),
		 statistics.pvariance(values),
		 statistics.pstdev(values))
		modelo.print()
		modelList.append(modelo)

	return modelList	
		

def valuesToNumeric(values):
	newValues = list()
	for value in values:
		try:
			newValues.append(float(value))
		except:
			if value != '': newValues.append(value)
	return newValues

if __name__ := '__main__':
	fileName = 'datos.csv'
	file = open(fileName, newline='')
	descriptiva_datos(file)