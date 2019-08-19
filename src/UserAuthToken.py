import Db
import json
import AccessToken

class UserAuthToken():
  def __init__(self):
    self.db = Db.connect()
  
  def user_auth_token(self , json_data):
    cur = self.db.cursor()
    data = json.loads(json_data)
    user_id = data["user_id"]


    # user_idからaccess_tokenを取得
    get_token = AccessToken.get_token(user_id)

    # トークンを比較
    if(get_token == data["access_token"]):
      return True
    else:
      return False