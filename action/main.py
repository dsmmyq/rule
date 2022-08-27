import requests

rawnetflix = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Netflix/Netflix.yaml").text

result = rawnetflix.split("\n") 

with open("./netflix.yaml", "w") as f:
    f.write("\n".join(result))
