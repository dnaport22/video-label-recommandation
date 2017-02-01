from AudioConverter import *
from VideoConverter import *


class Main(AudioConverter, VideoConverter):
	__AC = AudioConverter()
	__VC = VideoConverter()

	__VIDEO_FILE = None
	__AUDIO_FILE = None
	__output_name = None
	__output_format = None

	def load(self, video_file, output_name, output_format):
		self.__setVideoFile(video_file)
		self.__setOutputName(output_name)
		self.__setFormat(output_format)

	def getAudioFromVideo(self):
		if self.__getFormat() == 'wav':
			self.__setAudioFile(
				self.__getOutputName(),self.__getFormat()
				)

			return self.__getVideoConverter().convertToWav(
				self.__getVideoFile(), 
				self.__getOutputName()
				)

		if self.__getFormat() == 'mp3':
			self.__setAudioFile(
				self.__getOutputName(),self.__getFormat()
				)

			return self.__getVideoConverter().convertToMp3(
				self.__getVideoFile(),
				self.__getOutputName()
				)

	def getTextFromAudio(self):
		return self.__getAudioConverter().convertAudioToText(
			self.__getAudioFile(), self.__getOutputName()
			)

	def __setFormat(self, format):
		Main.__output_format = format

	def __setOutputName(self, name):
		Main.__output_name = name

	def __setVideoFile(self, video):
		Main.__VIDEO_FILE = video

	def __setAudioFile(self, video_file, format):
		Main.__AUDIO_FILE = video_file + '.' + format

	def __getAudioFile(self):
		return Main.__AUDIO_FILE

	def __getVideoFile(self):
		return Main.__VIDEO_FILE

	def __getFormat(self):
		return Main.__output_format

	def __getOutputName(self):
		return Main.__output_name

	def __getVideoConverter(self):
		return Main.__VC

	def __getAudioConverter(self):
		return Main.__AC

x = Main()
x.load('test.mp4', 'sample', 'wav')
x.getAudioFromVideo()
x.getTextFromAudio()

