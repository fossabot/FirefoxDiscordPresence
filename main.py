import time, pathlib, json, rpc, lz4.block
from pathlib import Path

class FirefoxRichPresence():
	def __init__(self):
		self.rpc_obj = rpc.DiscordIpcClient.for_platform("Client_ID")
		print("Rich Presence is now live")

		self.filepath = next(Path("C:/Users/{0}/AppData/Roaming/Mozilla/Firefox/Profiles/".format(os.getlogin())).glob("*.default/sessionstore-backups/recovery.jsonlz4"))

		self.update_freq = 45 # Seconds before getting tab info

		self.GetTabs()

	def GetTabs(self):
		sites = ["twitter","facebook"]

		f = open(self.filepath, "rb")
		magic = f.read(8)
		data = json.loads(lz4.block.decompress(f.read()).decode("utf-8"))
		f.close()

		for win in data.get("windows"):
			for tab in win.get("tabs"):
				i = tab.get("index") - 1
				url = tab.get("entries")[i].get("url")
				title = tab.get("entries")[i].get("title")
				for site in sites:
					if site in url:
						self.SetPresence(site.capitalize(), url, site+"_", title)
						break

	def SetPresence(self, site, url, image, image_text):
		print("Image: {0}\nSite: {1}\nURL: {2}\n".format(image, site, url))
		start_time = time.time()
		while True:
			activity = {
					"state": url,
					"details": site,
					"timestamps": {
						"start": start_time
					},
					"assets": {
						"small_text": image_text,
						"small_image": image,
						"large_text": site,
						"large_image": image
					}
				}
			self.rpc_obj.set_activity(activity)
			time.sleep(self.update_freq)
			self.GetTabs()

FirefoxRichPresence()
