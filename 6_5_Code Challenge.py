import requests
from bs4 import BeautifulSoup

keywords = [
	"flutter",
	"python",
	"golang"
]

url = "https://remoteok.com/remote-flutter-jobs"

# headers 변경해서 request
r = requests.get(url, headers = {
    "User-Agent" : "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36"
}
)


print(r.status_code)
# print(r.content)