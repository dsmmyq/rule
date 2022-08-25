import requests

rawSpeedtest= requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Speedtest/Speedtest.yaml").text

result = rawSpeedtest.split("\n")

with open("./Speedtest.yaml", "w") as f:
    f.write("\n".join(result))

