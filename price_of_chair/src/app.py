import requests


request = requests.get("http://www.google.com")


print(request.content)