import sys
import demo_main_file as dmf
import requests
import json

API_KEY="15610bbe7d43a41240679410cdfbcf44"
TOKEN="511b4c4f867f79ec67ccfcb66f2b097640c6f3165c1fbf2d5a81369bc6b7c67d"
BOARD_NAME="B1"
ORG_NAME="teamrud"
content_file=sys.argv[1]
list_name=sys.argv[2]
card_name=sys.argv[3]

with open(content_file, 'r')as comment_content_file:
	data=comment_content_file.read()

dmf.initialize(apikey=API_KEY, token=TOKEN, board_name=BOARD_NAME, org_name=ORG_NAME)

def get_cardid(card_name, lid):
	try:
	  	resp = requests.get("https://api.trello.com/1/lists/%s/cards" % (lid), params=dict(key=API_KEY, token=TOKEN))
	  	resp.raise_for_status()
	  	respo=json.loads(resp.content)
	  	for ca in respo:
			if card_name==ca['name']:
				return ""+ca['id']

	except:
		print("get_cardid: operation failed")
		exit(1)
	

def add_comment(card_name, comment):
	try:
	  	lid=dmf.get_listid(list_name)
	  	cid=get_cardid(card_name=card_name, lid=lid)
	  	resp = requests.post("https://api.trello.com/1/cards/%s/actions/comments" % (cid), params=dict(key=API_KEY, token=TOKEN), data=dict(text=comment))
	  	resp.raise_for_status()
	  	json.loads(resp.content)

	except:
            	print("add_comment: operation failed")
	    	exit(1)

add_comment(card_name=card_name, comment=data)


