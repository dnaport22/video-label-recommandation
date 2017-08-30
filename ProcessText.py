import os
import nltk
from nltk.corpus import stopwords
import requests
import json

GCLOUD_CONSTS = {
    "GCLOUD_NLP":{
        "URL": "https://language.googleapis.com/v1/documents:analyzeEntities?key=",
        "CONTENT-TYPE": "application/json"
    }
}

class ProcessText():
	def __init__ (self):
		self.stop = set(stopwords.words('english'))

	def textAnalyser(self):
		fl = open('sample.txt', 'rb')
		for words in fl:
			text = words

		text = nltk.word_tokenize(text)
		tags = nltk.pos_tag(text)
		propernouns = [word for word,pos in tags if pos == 'NN']

			# return "Raw:: ",words
		#nlp_words = [i for i in text if i not in self.stop]

		return propernouns

	def process_text_using_cloud(self, text):

		class GCLOUD_Processing():
			'''
			Text processing using Google Cloud's Natural Language Processing API
			'''

			# Request data
			_REQ = None

			# Payload
			_DATA = None

			@classmethod
			def load_data(cls, data):
				'''Setting up payload data and preparing data in GCloud required format.'''
				cls._DATA = data
				cls._prepare_data()

			@classmethod
			def _prepare_data(cls):
				'''Preparing data in GCloud required format.'''
				cls._DATA = json.dumps({"document": {
					"type": "PLAIN_TEXT",
					"content": cls._DATA
				}})

			@classmethod
			def execute_call(cls):
				'''Creating a post request to GCould using Requests module.'''
				url = GCLOUD_CONSTS['GCLOUD_NLP']['URL']
				headers = {
					"Content-Type": GCLOUD_CONSTS['GCLOUD_NLP']['CONTENT-TYPE']
				}

				cls._REQ = requests.post(url, data=cls._DATA, headers=headers)

			@classmethod
			def retrieve_response(cls):
				'''
				:return: json | response on the request made to GCloud using execute_call method.
				'''
				return cls._REQ.json()

		GCLOUD_Processing.load_data(text)
		GCLOUD_Processing.execute_call()
		return GCLOUD_Processing.retrieve_response()

x = ProcessText()

with open('sample.txt', 'rb') as fl:
		for words in fl:
			text = words
features = x.process_text_using_cloud(text)
fit = {}
for elems in features['entities']:
	fit[elems['name']] = elems['salience']

count, total = 0, 1
for k, v in fit.iteritems():
	count += 1
	total += v

avg_salience = total/count

for k, v in fit.iteritems():
	if v > avg_salience:
		print k