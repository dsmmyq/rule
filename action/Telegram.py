import requests

rawTelegram = requests.get("https://raw.githubusercontent.com/Loyalsoldier/clash-rules/release/telegramcidr.txt").text

result = rawTelegram.split("\n")

with open("./Telegram.yaml", "w") as f:
    f.write("\n".join(result))
