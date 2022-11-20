import requests

r = requests.get("https://www.tele.soumu.go.jp/musen/list/ST=1&DA=1&SC=1&DC=1&OF=2&OW=FB_H&IT=E&NA=%8Ay%93V%83%82%83o%83C%83%8B")

print(r.json())
