import Libs.crawler as crawler
import Libs.Twitter as Twitter

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

	novos = crawler.removerDadosDesnecessarios( diff )
	if len(novos) > 0:
		print(list(map(lambda x: x['mensagem'], novos)))
	else:
		print('-')
	print("\n")

	for commit in novos:
		Twitter.tweetar(Twitter.formatarEmTweet(commit))

	time.sleep(61) # Execute essa operação a cada um minuto + 1 segundo
