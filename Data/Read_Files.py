class ReadFiles:
	fileName = "Data/KnownWords.txt"
	lines = []
	def readLinesOfWords(self):
		with open(self.fileName, "r") as self.fileOpen:

			for line in self.fileOpen:
				self.lines.append(line)
				self.lines = [x.strip() for x in self.lines]



	def addToFiles(self):
		with open(self.fileName, "a") as self.fileOpen2:

			for i in self.fileOpen2:
				self.fileOpen2.write(i + "\n")

	def compareFiles(self, listPulled):
		self.readLinesOfWords()
		self.listPulled = listPulled
		self.clearExtraWords = set(self.lines).intersection(self.listPulled)
		self.turnToList = list(self.clearExtraWords)