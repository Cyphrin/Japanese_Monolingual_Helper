import requests

class GetWebsite:

	def __init__(self, website, searchedWord):
		self.completedWebsiteName = website + searchedWord

	@property
	def connectToWebsite(self):
		try:
			self.makeCall = requests.get(self.completedWebsiteName, timeout=3.0)
			self.makeCall.raise_for_status()
		except requests.exceptions.Timeout as errt:
			return errt  # "Timed Out"
		except requests.exceptions.ConnectionError as errc:
			return errc  # "Connection Error"
		except requests.exceptions.HTTPError as errh:
			return errh  # "HTTP Error"
		except requests.exceptions.RequestException as err:
			return err  # "Something is wrong"
		else:
			return self.makeCall