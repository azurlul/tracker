import requests
import time
import json
import datetime
import os

# replace with your own Clash of Clans API token
token = ""

# replace with your own webhook
webhook_url = ""

# read player tags and initial names from players.json file
with open("players.json", encoding="utf-8") as f:
    players = json.load(f)

while True:
    invalid_tags = []
    try:
        for player in players:
            try:
                player_url = f"https://api.clashofclans.com/v1/players/%23{player['tag']}"
                player_response = requests.get(player_url, headers={"Authorization": f"Bearer {token}"}).json()
                
                if player_response["name"] != player["name"]:
                    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    log_message = f"[DETECTED]: {timestamp} | #{player['tag']} | Old NC: {player['name']} | New NC: {player_response['name']}\n"
                    print(log_message)
                    payload = {
                        "embeds": [
                            {
                                "title": f":detective: **DETECTED**",
                                "description": f"**#{player['tag']}** | __**Old NC:**__ `{player['name']}` | __**New NC:**__ `{player_response['name']}`",
                                "color": 0x00ff00,
                                "footer": {
                                    "text": "#AzurOnTop!"
                                },
                                "timestamp": timestamp
                            }
                        ]
                    }
                    requests.post(webhook_url, json=payload)
                    player["name"] = player_response["name"]
                    # append log message to name_changes.log file
                    with open("nc.log", "a", encoding="utf-8") as log_file:
                        log_file.write(log_message)
                else:
                    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    log_message = f"[NOTHING]: {timestamp} | #{player['tag']} | {player['name']}\n"
                    print(log_message)
                    
            except KeyError:
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                log_message = f"[BANNED]: {timestamp} | #{player['tag']} ({player['name']}) has been banned!\n"
                print(log_message)
                payload = {
                    "embeds": [
                        {
                            "title": f":bangbang: **BANNED**",
                            "description": f"**#{player['tag']} (`{player['name']}`) has been banned!**",
                            "color": 0xff0000,
                            "footer": {
                                "text": "#AzurOnTop!"
                            },
                            "timestamp": timestamp
                        }
                    ]
                }
                requests.post(webhook_url, json=payload)
                with open("ban.log", "a", encoding="utf-8") as log_file:
                    log_file.write(log_message)
                invalid_tags.append(player['tag'])  # add invalid tag to list

        players = [p for p in players if p['tag'] not in invalid_tags]

        with open("players.json", "w", encoding="utf-8") as f:
            json.dump(players, f, ensure_ascii=False)

        for i in range(180, 0, -1):
            minutes = i // 60
            seconds = i % 60
            print(f"[CHECKING]: {minutes:02}:{seconds:02}")
            time.sleep(1)
            os.system('cls' if os.name == 'nt' else 'clear')
        os.system('cls' if os.name == 'nt' else 'clear')

    except Exception as e:
        print(f"Error occurred: {e}\n")
        time.sleep(60)
