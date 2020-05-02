from Get_Website import GetWebsite
from bs4 import BeautifulSoup

def getSynonym(synonym):
	weblioSite = "https://thesaurus.weblio.jp/content/"
	listOfSynonyms = []

	# Make a call to website. Check for connection to site.
	websiteCall = GetWebsite(weblioSite, synonym)
	soup = BeautifulSoup(websiteCall.connectToWebsite.content, "html.parser")
	pullTagsFromSite = soup.find_all("td", {"class": "nwntsR"})

	# First set of loops Grabs all the words that aren't in "a" tags and put them in the list
	for container1 in pullTagsFromSite:
		for wordsWithNoTags in container1:
			if (wordsWithNoTags.find("a") == -1 and wordsWithNoTags.find("・") == -1
					and wordsWithNoTags.find("A") == -1 and wordsWithNoTags != " "):
				listOfSynonyms.append(wordsWithNoTags)

	# Second set of loops grabs all the words that are in "a" tags and puts them in the list
	for container2 in pullTagsFromSite:
		synonymWordsWithTags = container2.findAll("a")
		for individualWord in synonymWordsWithTags:
			listOfSynonyms.append(individualWord.get_text())

	# This for loop returns the the list with whitespace removed.
	return [removingWhiteSpace.strip(' ') for removingWhiteSpace in listOfSynonyms]