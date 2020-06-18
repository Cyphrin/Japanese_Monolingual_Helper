from View.GUI_View import View
from Data.Thesaurus import Thesaurus
from Data.Read_Files import ReadFiles

try:
	import tkinter as tk
except ImportError:  # python 2
	import Tkinter as tk


class Controller(tk.Listbox):
	data = Thesaurus()


	def __init__(self):
		self.view = View(self)


	# Function makes call to Gui_View to start the mainloop() to show the GUI.
	def main(self):
		self.view.main()

	def onButtonClick(self):
		self.resultsBox()
		self.comparedWordsList()

	# This function makes a call From Data.Thesaurus to the Thesaurus class to
	# input the web tags and the specific site to retrieve the data for synonyms.
	def getSynonym(self):
		self.data.webTag1 = "td"
		self.data.webTag2 = "class"
		self.data.webTag3 = "nwntsR"
		self.data.makeCallToSite("https://thesaurus.weblio.jp/content/", self.view.value_var.get())
		self.data.loopThroughThesaurus()

	# This function makes a call From Data.Thesaurus to the Thesaurus class to
	# input the web tags and the specific site to retrieve the data for antonyms.
	def getAntonym(self):
		self.data.webTag1 = "span"
		self.data.webTag2 = "class"
		self.data.webTag3 = "wtghtAntnm"
		self.data.makeCallToSite("https://thesaurus.weblio.jp/antonym/content/", self.view.value_var.get())
		self.data.loopThroughThesaurus()

	# This function is displaying the data that is retrieved from functions getSynonym and getAntonym.
	def resultsBox(self):

		if self.view.rbValue.get() == 1:
			self.getSynonym()
			self.view.displayResultsBox(self.view.tab1)
			self.view.showResults(self.data.finalList)

		else:
			self.getAntonym()
			self.view.displayResultsBox(self.view.tab1)
			self.view.showResults(self.data.finalList)

	# Function compares the Words you already know in your list with words that are generated
	def comparedWordsList(self,):
		readFiles = ReadFiles()
		readFiles.compareFiles(self.data.finalList)
		self.view.displayResultsBox(self.view.tab2)
		self.view.showResults(readFiles.turnToList)

if __name__ == '__main__':
	monolingualApp = Controller()
	monolingualApp.main()
