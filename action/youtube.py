import requests

rawYoutube = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/YouTube/YouTube.yaml").text

result = rawYoutube.split("\n")

with open("./youtube.yaml", "w") as f:
    f.write("\n".join(result))
