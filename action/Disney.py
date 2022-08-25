import requests

rawDisney = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Disney/Disney.yaml").text

result = rawDisney.split("\n")

with open("./Disney.yaml", "w") as f:
    f.write("\n".join(result))
