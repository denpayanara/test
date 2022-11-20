import json
import urllib.request
import ssl

url = 'https://www.tele.soumu.go.jp/musen/list?ST=1&DA=1&SC=1&DC=1&OF=2&OW=FB_H&IT=E&NA=%8Ay%93V%83%82%83o%83C%83%8B'

ctx = ssl.create_default_context()
ctx.options |= 0x4  # ssl.OP_LEGACY_SERVER_CONNECT

# req = urllib.request.urlopen(url, context=ctx)

try:
    with urllib.request.urlopen(url, context=ctx) as res:
        print(res.read())
except urllib.error.HTTPError as err:
    print(err.code)
except urllib.error.URLError as err:
    print(err.reason)
