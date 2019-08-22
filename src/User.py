import uuid
import Db

# メールアドレスからuser_id取得
def get_user_id(data):
  db = Db.connect()
  cur = db.cursor()
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

  return rows[0]