# -*- coding: utf-8 -*-
import requests
import datetime, calendar
from functools import reduce

def dataParaUnixtimestamp(original):
	'''
		Esta função retorna um Unixtimestamp equivalente a data passada
		2018-09-10T19:29:40. -> 1536618580

		original -- A data a ser convertida
	'''
	return int(calendar.timegm(datetime.datetime.strptime(original.split('.')[0], "%Y-%m-%dT%H:%M:%S").timetuple()))

def buscarCommits(query):
	'''
		Esta função retorna uma lista de Dicionários(Dict) contendo os commits q contém a palavra passada

		query -- A palavra que deve ser usada na busca
	'''
	hoje = datetime.datetime.now().strftime("%Y-%m-%d")

	acumulado = []
	
	for palavra in query:
		acumulado = acumulado + requests.get(
									"https://api.github.com/search/commits?q="+palavra+"+committer-date:"+hoje+".."+hoje+"&sort=committer-date",
									headers={
												'Accept': 'application/vnd.github.cloak-preview',
												'Time-Zone': 'America/Sao_Paulo'
											}
								).json()['items']

	return acumulado

def diffCommitsAnteriores(novos, anteriores):
	'''
		Esta função retorna uma versão filtrada dos commits passados baseada na data mínima

		todos -- A lista de commits
		apartir -- A data(str) a partir da qual o filtro deve ser aplicado
	'''
	codsAnteriores = map(lambda x: x['sha'], anteriores)

	return list(filter(lambda x: x['sha'] not in codsAnteriores, novos))

def removerDadosDesnecessarios(bruto):
	final = []
	for commit in bruto:
		final.append({
			'mensagem': commit['commit']['message'],
			'url': commit['html_url']
			})
	return final
