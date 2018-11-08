# coding: UTF-8
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

# TODO: ここloopで簡略化できないかな？増えてきたら検討
SLACK_API_TOKEN = os.environ.get("SLACK_API_TOKEN")
USER_ID = os.environ.get("USER_ID")
