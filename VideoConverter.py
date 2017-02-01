import os

class VideoConverter():
	__ENCODER = "ffmpeg"

	def convertToMp3(self, audio, output_name):
		os.system(
			"%s -i %s -q:a 0 -map a %s.mp3"
			%(self.__getEncoder(),audio,output_name))

	def convertToWav(self, audio, output_name):
		os.system(
			"%s -i %s -acodec pcm_s16le -ar 44100 %s.wav"
			%(self.__getEncoder(),audio,output_name))

	def __getEncoder(self):
		return VideoConverter.__ENCODER