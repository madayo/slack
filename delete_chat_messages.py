#coding utf-8

# slackのメッセージを一括削除する
# private, publicどちらにも対応しており、対話式で削除対象とするチャンネルを指定する。
# starがついているものは削除対象外

import requests
import json
import time
from settings import SLACK_API_TOKEN

def get(url, params):
  req = requests.get(url, params)
  return req.json()

token = SLACK_API_TOKEN
params = {"token" : token}

print("channel is private or public? 1:private, 2:public")
target = "groups" if input("input number >> ") == "1" else "channels"

data = get("https://slack.com/api/%s.list" % target, params)

for i, d in enumerate(data[target]):
  print(str(i+1) + " --> " +d["name"])
channel = int(input("input number >> ")) - 1
channel = data[target][channel]["id"]

params = {"token" : token, "channel" : channel, "count" : 1000 }
data = get("https://slack.com/api/%s.history" % target, params)
for d in data["messages"]:
 # スター付きは削除しない
  if "is_starred" in d and d["is_starred"]:
    continue

  delete_params = {"token" : token, "channel" : channel, "ts" : d["ts"]}
  result = get("https://slack.com/api/chat.delete", delete_params)
  print(result)
  # 連続で送りすぎるとエラーになるので1秒待機
  time.sleep(1)
