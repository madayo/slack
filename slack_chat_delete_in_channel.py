#coding: utf-8

# slackのメッセージを一括削除する
# private, publicどちらにも対応しており、対話式で削除対象とするチャンネルを指定する。
# starがついているものは削除対象外
# 実行前にプログラム内のtoken変数に適切な値を入力すること https://api.slack.com/custom-integrations/legacy-tokens

import urllib
import urllib2
import json
import time

def curl(url, params):
  params = urllib.urlencode(params)
  req = urllib2.Request(url)
  req.add_header('Content-Type', 'application/x-www-form-urlencoded')
  req.add_data(params)

  res = urllib2.urlopen(req)

  body = res.read()
  return json.loads(body)

token = ''

print 'channel is private or public? 1:private, 2:public'
target = 'groups' if input('input number >> ') == 1 else 'channels'

data = curl("https://slack.com/api/%s.list" % target, { 'token' : token })

for i, d in enumerate(data[target]):
  print str(i+1) + " --> " +d["name"]
print "Which channels messages wanna delete? "
channel = input('input number >> ')
channel = data[target][channel-1]["id"]


data = curl("https://slack.com/api/%s.history" % target, { 'token' : token, 'channel' : channel, 'count' : 1000 })
for d in data['messages']:
  # スター付きは削除しない
  if "is_starred" in d and d["is_starred"]:
    continue

  result = curl("https://slack.com/api/chat.delete", { 'token' : token, 'channel' : channel, 'ts' : d['ts']})
  print(result)
  #連続で送りすぎるとエラーになるので1秒待機
  time.sleep(1)
