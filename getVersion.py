import requests
print(requests.__version__)

googleHome = requests.get("http://google.com/")

print(googleHome.text)