import os
import nltk
from nltk.corpus import stopwords

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

x = ProcessText()
print x.textAnalyser()
