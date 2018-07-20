import demo_main_file
import os

demo_main_file.create(key="apikey", token="token", board_name="phone name", org_name="org", list_name=os.environ['PARAM_CUSTOMER'], card_name=os.environ['BUILD-DISPLAY-NAME'], card_description=os.environ['CARD_DESC'], card_comment="jenkins url")
