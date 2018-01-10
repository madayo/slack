#coding utf-8

# slackのメッセージを一括削除する
# private, publicどちらにも対応しており、対話式で削除対象とするチャンネルを指定する。
# starがついているものは削除対象外
# 実行前にプログラム内のtoken変数に適切な値を入力すること https://api.slack.com/custom-integrations/legacy-tokens

import requests
import json
import time

def get(url, params):
  req = requests.get(url, params)
  return req.json()

token = "xoxp-150069085396-150031593506-296521270242-67db28316330e71ab947265b54b3f02f"
params = {'token' : token}

print("channel is private or public? 1:private, 2:public")
target = "groups" if input("input number >> ") == 1 else "channels"

data = get("https://slack.com/api/%s.list" % target, params)

for i, d in enumerate(data[target]):
  print(str(i+1) + " --> " +d["name"])
channel = int(input('input number >> ')) - 1
channel = data[target][channel]["id"]

params.update({"channel" : channel})
data = get("https://slack.com/api/%s.history" % target, params)
for d in data['messages']:
 # スター付きは削除しない
  if "is_starred" in d and d["is_starred"]:
    continue

  delete_params = params
  delete_params.update({"ts" : d["ts"]})
  result = get("https://slack.com/api/chat.delete", delete_params)
  print(result)
  # 連続で送りすぎるとエラーになるので1秒待機
  time.sleep(1)
