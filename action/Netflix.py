import requests

rawNetflix = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Netflix/Netflix.yaml").text

result = rawNetflix.split("\n") 

with open("./Netflix.yaml", "w") as f:
    f.write("\n".join(result))
