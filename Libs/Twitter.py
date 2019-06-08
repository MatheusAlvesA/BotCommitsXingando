# -*- coding: utf-8 -*-
import tweepy 
  
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""

def getAPI():
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
  
	auth.set_access_token(access_token, access_token_secret)
	return tweepy.API(auth)

def formatarEmTweet(original):
	mensagem = original['mensagem'][:200]
	if len(original['mensagem']) >= 200:
		mensagem += '...'
	mensagem += "\n\n"
	mensagem += '#CommitXingando #GitHub'
	# Não mostrar o link do commit por questão de privacidade
	#mensagem += "\nLink: " + original['url']
	return mensagem

def tweetar(mensagem):
	try:
		api = getAPI()
		api.update_status(status = mensagem)
		return True
	except:
		return False