from trello import *

user=TrelloClient(api_key=" ",token=" ")
board_id=""
lname=""
cname=""
cdesc=""
ccomment=""
lid=""
apikey=""
tok=""

def create(key, token, board_name, org_name, list_name, card_name, card_description, card_comment):#just invoke this method rest will take care all by itself
	global key
	apikey=key
	global tok
	tok=token
	global user
	user = TrelloClient(api_key=apikey,token=tok)
	global board_id
	board_id=get_boardid(board_name=board_name, org_name=org_name)
	global lname
	lname=list_name
	global cname
	cname=card_name
	global cdesc
	cdesc=card_description
	global ccomment
	ccomment=card_comment
	new_list()
	new_card()
	

def get_boardid(board_name, org_name):
	resp = requests.get("https://api.trello.com/1/organizations/%s/boards" % (org_name), params=dict(key=key, token=token))
	resp.raise_for_status()
	respo=json.loads(resp.content)
	for board in respo:
	  if board_name==board['name']:
	     return ""+board['id']
	     break;


def new_list():#if list 'lname' not exists:creates a list 'lname' else return back to create
	if not isLexist():
	  nl=Board(client=user,board_id=board_id)
	  nl.add_list(lname)
	else:
	  return

def isLexist():
	li_name="<List "+lname+">"
	l=Board(client=user, board_id=board_id)
	all_lists=l.all_lists()
	lst=''.join(str(all_lists))
	if li_name in lst:
	  return True
	else:
	  return False

def isCexist():
	cr_name="<Card "+cname+">"
	c=List(board=user,list_id=lid)
	all_c=c.list_cards(card_filter="all")
	clst=''.join(str(all_c))
	print(clst)
	if cr_name in clst:
	  return True
	else:
	  return False
	


def get_listid():
	resp = requests.get("https://api.trello.com/1/boards/%s/lists" % (board_id), params=dict(key=apikey, token=tok))
	resp.raise_for_status()
	respo=json.loads(resp.content)
	print respo
	for li in respo:
		if lname==li['name']:
		  return li['id']

	

def new_card():#if card 'cname' not exists create a card 'cname' else quit
	global lid
	lid=get_listid()
	if not isCexist():
	  l=List(board=user, list_id=lid)
	  l.add_card(name=cname, desc=cdesc, position="top")#no comment parameter in the lib so ill add the comment later
	else:
	  exit(0)

#pending tasks: creating a delete method(to delete card) and updating comment of the card
#feeling sleepy bro its almost 1am, ill do these two tasks in the morning ;)
	
	
	

	
	  


	
	







