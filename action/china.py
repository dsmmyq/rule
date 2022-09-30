import requests

rawchina = requests.get("https://raw.githubusercontent.com/felixonmars/dnsmasq-china-list/master/accelerated-domains.china.conf").text
rawchina = rawchina.replace("server=/","").replace("/114.114.114.114","")

result = rawchina.split("\n")

with open("./china.txt", "w") as f:
    f.write("\n".join(result))
