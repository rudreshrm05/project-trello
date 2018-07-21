import demo_main_file
import os

initialize(apikey="yourkey", token="your-token", board_name="boardname", org_name="organization name")#you only need to initialize your api, token, bname and org name once

new_list(list_name"List 1")

new_card(card_name="Card1", list_name="List 1", desc="new card")

add_comment(card_name="Card1", comment="iron man")

add_comment(card_name="Card1", comment="Captain america")

new_card(card_name="Card2", list_name="List 1", desc="new card")

add_comment(card_name="Card2", comment="Super man")


