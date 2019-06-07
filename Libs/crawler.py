# -*- coding: utf-8 -*-
import requests
import datetime, calendar

def dataParaUnixtimestamp(original):
	'''
		Esta função retorna um Unixtimestamp equivalente a data passada
		2018-09-10T19:29:40. -> 1536618580

		original -- A data a ser convertida
	'''
	return int(calendar.timegm(datetime.datetime.strptime(original, "%Y-%m-%dT%H:%M:%S.").timetuple()))

def buscarCommits(query):
	'''
		Esta função retorna uma lista de Dicionários(Dict) contendo os commits q contém a palavra passada

		query -- A palavra que deve ser usada na busca
	'''
	try:
		r = requests.get(
							"https://api.github.com/search/commits?q="+query+"&sort=committer-date",
							headers={'Accept': 'application/vnd.github.cloak-preview'}
						)
	except Exception as e:
		return []

	if(r.status_code != requests.codes.ok):
		return []

	final = r.json()['items']

	return final

def filtrarCommitsApartirDe(todos, apartir):
	'''
		Esta função retorna uma versão filtrada dos commits passados baseada na data mínima

		todos -- A lista de commits
		apartir -- A data(str) a partir da qual o filtro deve ser aplicado
	'''
	
	timestampApartir = dataParaUnixtimestamp(apartir)

	return list(filter(lambda x: dataParaUnixtimestamp(x['commit']['committer']['date']) > timestampApartir, todos))

def removerDadosDesnecessarios(bruto):
	final = []
	for commit in bruto:
		final.append({
			'mensagem': commit['commit']['message'],
			'url': commit['html_url']
			})
	return final
