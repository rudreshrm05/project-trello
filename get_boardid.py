import requests
import json

def get_id(key, token, board_url):
	resp = requests.get(board_url+".json", params=dict(key=key, token=token))
	resp.raise_for_status()
	respo=json.loads(resp.content)
	print(respo['id'])

get_id(key="15610bbe7d43a41240679410cdfbcf44", token="511b4c4f867f79ec67ccfcb66f2b097640c6f3165c1fbf2d5a81369bc6b7c67d", board_url="https://trello.com/b/7O4Syx07/ruggear-10")
