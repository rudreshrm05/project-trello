import json
import requests

def get_listid(name, b_id):
	resp = requests.get("https://api.trello.com/1/boards/%s/lists" % (b_id), params=dict(key="15610bbe7d43a41240679410cdfbcf44", token="511b4c4f867f79ec67ccfcb66f2b097640c6f3165c1fbf2d5a81369bc6b7c67d"))
	resp.raise_for_status()
	respo=json.loads(resp.content)
	print respo
	for li in respo:
		if name==li['name']:
		  print li['id']

get_listid("l1","LHsTEgEu")


