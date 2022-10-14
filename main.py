import requests
import json

#https://rdb.altlinux.org/api/export/branch_binary_packages/sisyphus
#https://rdb.altlinux.org/api/export/branch_binary_packages/p10


req = requests.get("https://rdb.altlinux.org/api/export/branch_binary_packages/sisyphus")
data = req.content.decode()
req.close()

jsObj = json.loads(data)
with open("./data_file.json", mode="w", encoding="utf8") as f:
    f.write(json.dumps(jsObj, ensure_ascii=False))