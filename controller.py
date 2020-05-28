from View.GUI_View import View
from Data.Thesaurus import Thesaurus
try:
	import tkinter as tk
except ImportError:  # python 2
	import Tkinter as tk

class Controller(tk.Listbox):
	data = Thesaurus()

	def __init__(self):
		self.view = View(self)

	def main(self):
		self.view.main()

	def onButtonClick(self, caption):
		self.resultsBox()



	def getSynonym(self):
		self.data.webTag1 = "td"
		self.data.webTag2 = "class"
		self.data.webTag3 = "nwntsR"
		self.data.makeCallToSite("https://thesaurus.weblio.jp/content/", self.view.value_var.get())
		self.data.loopThroughThesaurus()


	def getAntonym(self):
		self.data.webTag1 = "span"
		self.data.webTag2 = "class"
		self.data.webTag3 = "wtghtAntnm"
		self.data.makeCallToSite("https://thesaurus.weblio.jp/antonym/content/", self.view.value_var.get())
		self.data.loopThroughThesaurus()


	def resultsBox(self):

		if self.view.rbValue.get() == 1:
			self.getSynonym()
			self.view.displayResults(self.data.final)

		else:
			self.getAntonym()
			self.view.displayResults(self.data.final)





if __name__ == '__main__':
	monolingualApp = Controller()
	monolingualApp.main()
