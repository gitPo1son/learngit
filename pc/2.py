from urllib.request import urlopen
import requests

data_get=requests.get("https://www.baidu.com").content.decode("utf-8")
html_url=urlopen("https://www.baidu.com")
data_url=html_url.read()
with open("data_get.html","w") as f:
    f.write(data_get)


print(data_get)
print("------------------------\n")
print(data_url)

with open("data_url.html","wb") as f:
    f.write(data_url)
