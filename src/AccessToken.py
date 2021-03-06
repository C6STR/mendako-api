import uuid
import Db

# トークン生成
def generate_token(user_id):
  # uuid
  access_token = str(uuid.uuid4())
  token_dict = {
    'user_id' : user_id,
    'access_token' : access_token
  }
  return token_dict

# トークン登録
def insert_token(user_id , access_token):
  db = Db.connect()
  cur = db.cursor()

  sql = """
    insert into access_token(
      user_id ,
      access_token
    )values(
      '%s',
      '%s'
    )
  """
  cur.execute(sql %(
    user_id ,
    access_token
  ))

  db.commit()

# トークン上書き
def update_token(token_dict):
  db = Db.connect()
  cur = db.cursor()

  sql = """
    update access_token set
      access_token = '%s'
      where user_id = '%s'
  """
  cur.execute(sql %(
    token_dict["access_token"],
    token_dict["user_id"]
  ))
  
  db.commit()

# user_idからaccess_tokenを取得
def get_token(user_id):
  db = Db.connect()
  cur = db.cursor()
  sql = """
    select access_token from access_token
    where user_id = '%s'
  """
  cur.execute(sql %(
    user_id
  ))
  rows = cur.fetchone()
  return rows[0]