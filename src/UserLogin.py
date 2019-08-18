import Db
import json
import UserGenerateToken

class UserLogin():
  def __init__(self):
    self.db = Db.connect()
  
  def user_login(self , json_data):
    cur = self.db.cursor()
    data = json.loads(json_data)

    sql = """
      select mail_address from user 
      where password = '%s' and
      mail_address = '%s'
    """
    cur.execute(sql %(
      data["password"],
      data["mail_address"]
    ))

    rows = cur.fetchone()
    token_dict = UserGenerateToken.generate_token(rows[0])
    
    return token_dict