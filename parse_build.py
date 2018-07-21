import xml.etree.ElementTree as ET
import re
import os
import sys
import demo_main_file as mf

API_KEY="15610bbe7d43a41240679410cdfbcf44"
TOKEN="511b4c4f867f79ec67ccfcb66f2b097640c6f3165c1fbf2d5a81369bc6b7c67d"
ORG_NAME="teamrud"
BOARD_NAME="ISF 1.0"

tree = ET.parse(sys.argv[1])
root = tree.getroot()
pc=(root.findall("actions/hudson.model.ParametersAction/parameters/hudson.model.StringParameterValue/[name='PARAM_CUSTOMER']"))[0]

os.environ['PARAM_CUSTOMER']=pc.find("value").text

bn=(root.findall("actions/org.jenkinsci.plugins.EnvironmentVarSetter/envVars/entry/string"))[1]
build_name=bn.text
mt=re.findall(r"\d{4}", build_name)
build_num=mt[0]

os.environ['JENKINS_URL']="https://build.isafe-mobile.com/job/"+sys.argv[2]+"/"+build_num+"/"


if re.match(r"[A-Za-z]", build_name)==None:
  card_name=os.environ['PARAM_CUSTOMER']+"-"+build_num+"-"+"unknown"
else:
  card_name=build_name

mf.initialize(apikey=API_KEY, token=TOKEN, board_name=BOARD_NAME, org_name=ORG_NAME)
mf.new_list(list_name=os.environ['PARAM_CUSTOMER'])
mf.new_card(card_name=card_name, list_name=os.environ['PARAM_CUSTOMER'])
mf.add_comment(card_name=card_name, comment=os.environ['JENKINS_URL'])






