import urllib.parse

import requests

Rakuten_4G = {
    # 1:免許情報検索  2: 登録情報検索
    "ST": 1,
    # 詳細情報付加 0:なし 1:あり
    "DA": 1,
    # スタートカウント
    "SC": 1,
    # 取得件数
    "DC": 1,
    # 出力形式 1:CSV 2:JSON 3:XML
    "OF": 2,
    # 無線局の種別
    "OW": "FB_H",
    # 所轄総合通信局
    "IT": "E",
    # 免許人名称/登録人名称
    "NA": "楽天モバイル",
}

def musen_api(d):

    parm = urllib.parse.urlencode(d, encoding="shift-jis")
    r = requests.get("https://www.tele.soumu.go.jp/musen/list", parm, verify=False)

    return r.json()

# Rakuten_4G

# データ取得
data_4G_1 = musen_api(Rakuten_4G)

print(data_4G_1)
