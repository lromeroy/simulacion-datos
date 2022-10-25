#!/usr/bin/env python3

import statistics
import csv

def descriptiva_datos(file):
	reader = csv.reader(file, delimiter=',')
	values = list()
	for row in reader:
		values += row
	values = valuesToNumeric(values)
	print('Valores: ', values)
	print('Ordenar:', sorted(values))
	print('Media: ', statistics.mean(values))
	print('Moda: ', statistics.mode(values))
	print('Mediana: ', statistics.median(values))
	print('Varianza: ', statistics.pvariance(values))
	print('Desviacion Estandard: ', statistics.pstdev(values))

def valuesToNumeric(values):
	newValues = list()
	for value in values:
		try:
			newValues.append(float(value))
		except:
			newValues.append(value)
	return newValues

if __name__ := '__main__':
	fileName = 'datos.csv'
	file = open(fileName, newline='')
	descriptiva_datos(file)