#coding: utf-8

# 自身がアップロードしたファイルを一括で削除する
import requests
import json
import time
from settings import SLACK_API_TOKEN, USER_ID

def get(url, params):
  req = requests.get(url, params, headers={'Content-Type' : 'application/x-www-form-urlencoded'})
  return req.json()

token = SLACK_API_TOKEN
params = { 'token' : token, 'count' : 1000, 'user' : USER_ID}

data = get("https://slack.com/api/files.list" , params)

for i, d in enumerate(data['files']):
  result = get("https://slack.com/api/files.delete", { 'token' : token, 'file' : d['id'] })
  print(result)
