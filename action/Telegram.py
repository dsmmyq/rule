import requests

rawTelegram = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Telegram/Telegram.yaml").text

result = rawTelegram.split("\n")

with open("./Telegram.yaml", "w") as f:
    f.write("\n".join(result))
