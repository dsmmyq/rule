import requests

rawYoutube = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/YouTube/YouTube.yaml").text
rawYoutube = rawYoutube.replace("IP-CIDR,172.110.32.0/21","").replace("- IP-CIDR,216.73.80.0/20","")
rawYoutube = rawYoutube.replace("IP-CIDR,IP-CIDR6,2620:120:e000::/40","")

result = rawYoutube.split("\n")

with open("./Youtube.yaml", "w") as f:
    f.write("\n".join(result))
