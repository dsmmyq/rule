import requests

rawGoogle = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Google/Google.yaml").text

rawYoutube = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/YouTube/YouTube.yaml").text
rawGoogle = rawGoogle.replace("DOMAIN-SUFFIX,yt.be","DOMAIN-KEYWORD,www.google.")
rawGoogle = rawGoogle.replace("DOMAIN-SUFFIX,ytimg.com","DOMAIN,lens.l.google.com")
rawGoogle = rawGoogle.replace("DOMAIN-SUFFIX,youtu.be","DOMAIN,www.googleapis.com")
rawGoogle = rawGoogle.replace("DOMAIN-SUFFIX,googlevideo.com","DOMAIN-SUFFIX,docs.google.com")
rawGoogle = rawGoogle.replace("DOMAIN-SUFFIX,ggpht.cn","DOMAIN-SUFFIX,drive.google.com")
rawGoogle = rawGoogle.replace("DOMAIN-SUFFIX,ggpht.com","DOMAIN-SUFFIX,googledrive.com")
rawYoutube = rawYoutube.replace("IP-CIDR,172.110.32.0/21","").replace("- IP-CIDR,216.73.80.0/20","")
rawYoutube = rawYoutube.replace("IP-CIDR,IP-CIDR6,2620:120:e000::/40","")
rawYoutube = rawYoutube.replace("payload:","")
result = rawGoogle.split("\n") + rawYoutube.split("\n")


with open("./Google.yaml", "w") as f:
    f.write("\n".join(result))
