import requests
print(requests.__version__)

googleHome = requests.get("http://google.com/")

print(googleHome)

gitHubCode = requests.get("https://raw.githubusercontent.com/mmcgoey/CMPUT-404-LABS/main/getVersion.py")

print(gitHubCode.text)