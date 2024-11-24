# Tracker

A simple python script to track players using <a href="https://developer.clashofclans.com/">Clash of Clans API</a> and <a href="https://www.youtube.com/watch?v=fKksxz2Gdnc">Discord Webhooks</a> to notify the user.<br/>
- Change the tags you want to track inside of **"players.json" (e.g: [{"tag": "XXX", "name": "xxx"}])** <br/>
- Replace **"apikey"** with your own API key to be able to make requests.<br/>
- If you wish to be notified on discord replace **"webhook_url"** with your own URL, if not results will be saved anyways in the logfiles. <br/>
- Additionally you can also change the cooldown before checking again with your desired time. (5 mins by default)<br/>

__Note:__ You're not obliged to add the names when creating the json structure, the script will fetch and add them automatically if you run it once.

### Running
```py
git clone https://github.com/azurlul/tracker.git
cd tracker
py tracker.py
```

### PoC
View inside of "nc.log" | Webhook result in Discord
--- | ---
![](img/1.png) | ![](img/2.png)
