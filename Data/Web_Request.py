import requests


class CheckWebRequest:

	def __init__(self):
		self.completedWebsite = ""

	def connectToWebsite(self):
		try:
			self.makeCall = requests.get(self.completedWebsite, timeout=3.0)
			print(self.makeCall.raise_for_status())
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
