#coding: utf-8

# slackのメッセージを一括削除する
# private, publicどちらにも対応しており、対話式で削除対象とするチャンネルを指定する。
# starがついているものは削除対象外
# 実行前にプログラム内のtoken変数に適切な値を入力すること https://api.slack.com/custom-integrations/legacy-tokens
# 実行前に自身のIDを確認してuser変数に適切な値を入力すること https://api.slack.com/methods/users.profile.get/test 画面右下くらいに@{自身のアカウント}リンクが表示されているのでクリックすることでIDを確認
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
user  = ''

data = curl("https://slack.com/api/files.list" , { 'token' : token, 'count' : 1000, 'user' : user })

for i, d in enumerate(data['files']):
  result = curl("https://slack.com/api/files.delete", { 'token' : token, 'file' : d['id'] })
  print result
