import sys
import config
from anixart import Anixart

anixart = Anixart()
anixart.login(login=config.login, password=config.password)

search_id = None

def get_user_info(search_id):
    return Anixart.get_user_info(anixart, user_id=search_id)