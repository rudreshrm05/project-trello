from trello import *

user=TrelloClient(api_key=" ",token=" ")
API_KEY=""
TOKEN=""
board_id=""
list_id=""


def initialize(apikey, token, board_name, org_name):
	global key
	API_KEY=key
	global tok
	TOKEN=token
	global user
	user = TrelloClient(api_key=API_KEY,token=TOKEN)
	global board_id
	board_id=get_boardid(board_name=board_name, org_name=org_name)
	

def get_boardid(board_name, org_name):
	resp = requests.get("https://api.trello.com/1/organizations/%s/boards" % (org_name), params=dict(key=key, token=token))
	resp.raise_for_status()
	respo=json.loads(resp.content)
	for board in respo:
	  if board_name==board['name']:
	     return ""+board['id']
	     break;


def new_list(list_name):
	if not isLexist(list_name):
	  nl=Board(client=user, board_id=board_id)
	  nl.add_list(list_name)
	else:
	  return


def isLexist(list_name):
	flag=False
	resp=request.get("https://api.trello.com/1/boards/%s/lists") % (board_id), params=dict(key=API_KEY, token=TOKEN))
	resp.raise_for_status()
	respo=json.loads(resp.content)
	for lst in respo:
	  if list_name==lst['name']
	    flag=True
	  else:
	    continue

	if flag==True:
	  return True
	else:
	  return False:


def isCexist(card_name):
	flag=False
	resp = requests.get("https://api.trello.com/1/lists/%s/cards" % (list_id), params=dict(key=API_KEY, token=TOKEN))
	resp.raise_for_status()
	respo=json.loads(resp.content)
	for ca in respo:
	  if card_name==ca['name']:
	    flag=True
	  else:
	    continue

	if flag==True:
	  return True
	else:
	  return False:
		

def get_listid(list_name):
	resp = requests.get("https://api.trello.com/1/boards/%s/lists" % (board_id), params=dict(key=API_KEY, token=TOKEN))
	resp.raise_for_status()
	respo=json.loads(resp.content)
	for li in respo:
		if lname==li['name']:
		  return ""+li['id']



def get_cardid(card_name):
	resp = requests.get("https://api.trello.com/1/lists/%s/cards" % (list_id), params=dict(key=API_KEY, token=TOKEN))
	resp.raise_for_status()
	respo=json.loads(resp.content)
	for ca in respo:
		if cname==ca['name']:
		  return ""+ca['id']


def add_comment(card_name, comment):
	cid=get_cardid(card_name)
	resp = requests.post("https://api.trello.com/1/cards/%s/actions/comments" % (cid), params=dict(key=API_KEY, token=TOKEN), data=dict(text=comment))
	resp.raise_for_status()
	json.loads(resp.content)

	

def new_card(card_name, list_name, desc):
	global list_id
	list_id=get_listid(list_name)
	if not isCexist(card_name):
	  l=List(board=user, list_id=lid)
	  l.add_card(name=card_name, desc=desc, position="top")	  
	else:
	  return

	
	
	

	
	  


	
	







