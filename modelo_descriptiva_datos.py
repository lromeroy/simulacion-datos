import statistics

class ModeloDescriptivaDatos:

	def __init__(self, valores, media, moda, mediana, varianza, desviacionEstandard):
		self.valores = valores
		self.media = media
		self.moda = moda
		self.mediana = mediana
		self.varianza = varianza
		self.desviacionEstandard = desviacionEstandard

	def print(self):
		print('Valores: ', self.valores)
		print('Ordenar:', sorted(self.valores))
		print('Media: ', self.media)
		print('Moda: ', self.moda)
		print('Mediana: ', self.mediana)
		print('Varianza: ', self.varianza)
		print('Desviacion Estandard: ', self.desviacionEstandard)
		print('\n')