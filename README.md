## FirefoxDiscordPresence
**Show currently open websites in Discord using Rich Presence**    

![Twitter Rich Presence](https://i.imgur.com/sy7JALQ.png)
![Reddit Rich Presence](https://i.imgur.com/aCFSMP5.png)
![Twitter Rich Presence Image](https://i.imgur.com/QwsKCiK.png)
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2FBenTearzz%2FFirefoxDiscordPresence.svg?type=shield)](https://app.fossa.io/projects/git%2Bgithub.com%2FBenTearzz%2FFirefoxDiscordPresence?ref=badge_shield)

### Requirements:
* lz4 (You can install it by using: `pip install lz4`)

----

### Sites:
You can specify the websites you want to be shown in the `GetTabs()` function in the `sites = [...]` list.
You can add anything to make it even more specific. `https`, `http`, `www`, `/some-link-after`.

To make it show ANY site you simply replace function `GetTabs()` with:
```python
    def GetTabs(self):
		f = open(self.filepath, "rb")
		magic = f.read(8)
		data = json.loads(lz4.block.decompress(f.read()).decode("utf-8"))
		f.close()

		for win in data.get("windows"):
			for tab in win.get("tabs"):
				i = tab.get("index") - 1
				url = tab.get("entries")[i].get("url")
				title = tab.get("entries")[i].get("title")
				self.SetPresence(site.capitalize(), url, "", title)
				break
```
This is what is being replaced:
```python
sites = ["twitter","facebook"] # Deleted line

	...
		for site in sites: 	 # Deleted line
			if site in url:	 # Deleted line
				self.SetPresence(site.capitalize(), url, "", title) # Fixed indent
				break 						    # Fixed indent
```

----

### Rich Presence image:
To change images depending on what site you're on, you simply find the images that you want, and add it as an asset for your [application](https://discordapp.com/developers/applications/).
Currently it's set to display `whateverTheSiteTitleIs_` (with an underscore at the end). So when I have Twitter open it uses image asset `"twitter_"`. If the image does not exist it will not show an error, but no image will be shown in rich presence.

----

### Update time:
The variable `self.update_freq` in the  `__init__` function specifies how long it takes before it will see currently open sites again. You can adjust it to your liking if you want it to update more/less frequently.   
***NOTE: Firefox tab data takes time to update, so it might not be accurate instantaneously***

----

### Credit:
The repo contains file `rpc.py` forked by [Suclearnub](https://github.com/suclearnub/python-discord-rpc) from ["Sublime Discord Rich Presence"](https://github.com/Snazzah/SublimeDiscordRP) made by [Snazzah](https://github.com/Snazzah).


## License
[![FOSSA Status](https://app.fossa.io/api/projects/git%2Bgithub.com%2FBenTearzz%2FFirefoxDiscordPresence.svg?type=large)](https://app.fossa.io/projects/git%2Bgithub.com%2FBenTearzz%2FFirefoxDiscordPresence?ref=badge_large)