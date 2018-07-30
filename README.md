# FirefoxDiscordPresence
Show currently open websites in Discord using Rich Presence

#### Requirements:
* lz4 `pip install lz4`

#### Sites:
You can specify the websites you want to be shown in the `GetTabs` function in `main.py` in the `sites = [...]` list.
You can add anything to the sites. `https`, `http`, `www`, `/some-link-after` to make it site specific.

To make it show ANY site you simply delete:
```python
# (line 28+29)
for site in sites:
    if site in url:
```

To change images you simply find the images that you want, and add it as an asset for your [application](https://discordapp.com/developers/applications/)
Currently it's set to display `whateverTheSiteTitleIs_` (with an underscore at the end). So when I have Twitter open it uses image asset `"twitter_"`. If the image does not exist it will not show an error, but no image will be shown in rich presence.


#### Update time:
The variable `self.update_freq` in the  `__init__` function specifies how long it takes before it will see currently open sites again. You can adjust to your liking if you want it to update more/less frequently.
