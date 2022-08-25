import requests

rawGoogle = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Google/Google.yaml").text

rawGoogle = rawGoogle.replace("DOMAIN-SUFFIX,yt.be","DOMAIN-KEYWORD,www.google.").replace("DOMAIN-SUFFIX,ytimg.com","DOMAIN,lens.l.google.com").replace("DOMAIN-SUFFIX,youtu.be","DOMAIN,www.googleapis.com").replace("DOMAIN-SUFFIX,ytimg.com","DOMAIN,lens.l.google.com").replace("DOMAIN-SUFFIX,googlevideo.com","DOMAIN-SUFFIX,docs.google.com").replace("DOMAIN-SUFFIX,ggpht.cn","DOMAIN-SUFFIX,drive.google.com").replace("DOMAIN-SUFFIX,ggpht.com","DOMAIN-SUFFIX,googledrive.com")

result = rawGoogle.split("\n")

with open("./Google.yaml", "w") as f:
    f.write("\n".join(result))