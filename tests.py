#!/usr/bin/env python3

from modelo_descriptiva_datos import ModeloDescriptivaDatos
import unittest
from descriptiva_datos import descriptiva_datos

class Tests(unittest.TestCase):
	
	def test_descriptiva_datos(self):
		tFile = open('datos_tests.csv', newline='')
		tExpectedResult = ModeloDescriptivaDatos(
			[1.73, 1.6, 1.4, 1.8, 1.75, 1.66, 1.55, 1.71, 1.42, 1.45],
			1.607,
			1.73,
			1.63,
			0.019201000000000006,
			 0.13856767299770897)
		
		tValues = descriptiva_datos(tFile)
		tModelValue = tValues[0]
		self.assertEqual(tModelValue.valores, tExpectedResult.valores)
		self.assertEqual(tModelValue.media, tExpectedResult.media)
		self.assertEqual(tModelValue.moda, tExpectedResult.moda)
		self.assertEqual(tModelValue.mediana, tExpectedResult.mediana)
		self.assertEqual(tModelValue.varianza, tExpectedResult.varianza)
		self.assertEqual(tModelValue.desviacionEstandard, tExpectedResult.desviacionEstandard)

if __name__ := '__main__':
	unittest.main()