import requests

rawGoogle = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/Google/Google.yaml").text
rawGoogleDrive = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/GoogleDrive/GoogleDrive.yaml").text
rawGoogleVoice = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/GoogleVoice/GoogleVoice.yaml").text
rawGoogleSearch = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/GoogleSearch/GoogleSearch.yaml").text
rawGoogleEarth = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/GoogleEarth/GoogleEarth.yaml").text
rawGoogleFCM = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/GoogleFCM/GoogleFCM.yaml").text
rawYoutube = requests.get("https://raw.githubusercontent.com/blackmatrix7/ios_rule_script/master/rule/Clash/YouTube/YouTube.yaml").text
rawGoogleDrive = rawGoogleDrive.replace("payload:","")
rawGoogleVoice = rawGoogleVoice.replace("payload:","")
rawGoogleSearch = rawGoogleSearch.replace("payload:","")
rawGoogleEarth = rawGoogleEarth.replace("payload:","")
rawGoogleFCM = rawGoogleFCM.replace("payload:","")
rawYoutube = rawYoutube.replace("payload:","")
result = rawGoogle.split("\n") + rawYoutube.split("\n") + rawGoogleDrive.split("\n") + rawGoogleVoice.split("\n") + rawGoogleFCM.split("\n") + rawGoogleSearch.split("\n") + rawGoogleEarth.split("\n")


with open("./Google.yaml", "w") as f:
    f.write("\n".join(result))
