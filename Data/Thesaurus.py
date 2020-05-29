from Data.Web_Request import CheckWebRequest
from bs4 import BeautifulSoup


class Thesaurus:
	checkWebRequest = CheckWebRequest()

	def __init__(self):
		self.websiteParser = "html.parser"
		self.webTag1 = ""
		self.webTag2 = ""
		self.webTag3 = ""
		self.listFromThesaurus = []

	# Makes call to specified site with a specified search word and
	# returns the html of the site based on tags the user inputs
	def makeCallToSite(self, website, searchedWord):
		self.website = website
		self.searchedWord = searchedWord
		self.checkWebRequest.completedWebsite = self.website + self.searchedWord
		self.connectionToWebsite = self.checkWebRequest.connectToWebsite()
		self.soup = BeautifulSoup(self.connectionToWebsite.content, self.websiteParser)
		self.pullTagsFromSite = self.soup.find_all(self.webTag1, {self.webTag2: self.webTag3})

	# Loops through Tags
	def loopThroughThesaurus(self):

		# Loops through tags and grabs all the words that don't have tags.
		for self.container1 in self.pullTagsFromSite:
			for self.wordsWithNoTags in self.container1:

				if (self.wordsWithNoTags.find("a") == -1 and self.wordsWithNoTags.find("・") == -1
						and self.wordsWithNoTags.find("A") == -1 and self.wordsWithNoTags != " "):
					self.listFromThesaurus.append(self.wordsWithNoTags)

		# Second set of loops grabs all the words that are in "a" tags and puts them in the list
		for self.container2 in self.pullTagsFromSite:
			self.thesaurusWordsWithTags = self.container2.findAll("a")
			for self.individualWord in self.thesaurusWordsWithTags:
				self.listFromThesaurus.append(self.individualWord.get_text())
				self.listFromThesaurus = list(dict.fromkeys(self.listFromThesaurus))


		self.almost = [removingWhiteSpace.strip(' ') for removingWhiteSpace in self.listFromThesaurus]
		self.finalList = list(dict.fromkeys(self.almost)) # Removes any duplicate words in list
		return self.finalList


