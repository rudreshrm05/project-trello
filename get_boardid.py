import requests
import json

def get_id(key, token, board_name, org_name):
	resp = requests.get("https://api.trello.com/1/organizations/%s/boards" % (org_name), params=dict(key=key, token=token))
	resp.raise_for_status()
	respo=json.loads(resp.content)
	for board in respo:
	  if board_name==board['name']:
	     print(board['id'])

get_id(key="15610bbe7d43a41240679410cdfbcf44", token="511b4c4f867f79ec67ccfcb66f2b097640c6f3165c1fbf2d5a81369bc6b7c67d", board_name="b1", org_name="exorg1")


