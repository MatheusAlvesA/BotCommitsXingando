import Libs.crawler as crawler
import time

def getListaPalavroes():
	f = open("listaPalavroes.txt", "r")
	bruto = f.read()
	f.close()
	lista = bruto.split("\n")
	return list(filter(lambda x: x[0] != '#',lista))

anteriores = []

while True:
	todos = []
	try:
		todos = crawler.buscarCommits(getListaPalavroes())
	except:
		pass

	diff = crawler.diffCommitsAnteriores(todos, anteriores)
	anteriores = todos

	print(crawler.removerDadosDesnecessarios( diff ))
	print("\n")
	time.sleep(61) # Execute essa operação a cada um minuto + 1 segundo
