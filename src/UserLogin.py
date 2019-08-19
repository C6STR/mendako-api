import Db
import json
import AccessToken

class UserLogin():
  def __init__(self):
    self.db = Db.connect()
  
  def user_login(self , json_data):
    cur = self.db.cursor()
    data = json.loads(json_data)

    sql = """
      select user_id from user 
      where password = '%s' and
      mail_address = '%s'
    """
    cur.execute(sql %(
      data["password"],
      data["mail_address"]
    ))

    rows = cur.fetchone()

    # トークン生成
    token_dict = AccessToken.generate_token(rows[0])
    # トークン上書き
    AccessToken.update_token(token_dict)

    return token_dict