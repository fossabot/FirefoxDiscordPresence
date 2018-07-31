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
						
		time.sleep(self.update_freq)
		self.GetTabs()

	def SetPresence(self, site, url, image, title):
		if len(site) + len(title) + 3 > 128:
			title = title[:125-(len(site)+3)] + "..."
			# If the "details" variable below goes over 128 characters total, Discord won't update rich presence
			# So we need to limit the number of characters which will be formatted like so: 
			# Twitter | Vsauce on Twitter: "The English language @Wikipedia as it existed on 7 April 2015 can be yours in hardcover form th..."
			# +3 compensates for the space between "Site | Title" which allows us to put "..." at the end if it's too long.

		activity = {
			"state": url,
			"details": "{0} | {1}".format(site, title),
			"timestamps": {
			"start": self.start_time
			},
			"assets": {
			"small_text": title,
			"small_image": image,
			"large_text": site,
			"large_image": image
			}
		}
		self.rpc_obj.set_activity(activity)
		time.sleep(self.update_freq)
		self.GetTabs()

FirefoxRichPresence()
