import speech_recognition as sr

class AudioConverter():
	__ENGINE = sr.Recognizer()

	__AUDIO = None
	__AUDIO_TEXT = None
	__OUTPUT_NAME = None

	def __processAudioFile(self, audio_file):
		with sr.AudioFile(audio_file) as source:
			return self.__getEngine().record(source)

	def convertAudioToText(self, audio, output_name):
		self.__setAudio(
			self.__processAudioFile(audio)
			)

		self.__setOutputName(output_name)

		self.__setAudioText(
			self.__getEngine().recognize_sphinx(
				self.__getAudio()
				)
			)

		return self.__generateFileOutput()

	def __generateFileOutput(self):
		fl = open(
			self.__getOutputName()+".txt",
			"w+"
			)

		fl.write(
			self.__getAudioText()
			)
		fl.close()

	def __setOutputName(self, name):
		AudioConverter.__OUTPUT_NAME = name

	def __setAudio(self, audio):
		AudioConverter.__AUDIO = audio

	def __setAudioText(self, text):
		AudioConverter.__AUDIO_TEXT = text

	def __getAudio(self):
		return AudioConverter.__AUDIO

	def __getOutputName(self):
		return AudioConverter.__OUTPUT_NAME

	def __getAudioText(self):
		return AudioConverter.__AUDIO_TEXT

	def __getEngine(self):
		return AudioConverter.__ENGINE

