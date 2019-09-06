import Db
import json

class DoneTask():
  def __init__(self):
    self.db = Db.connect()
  
  def done_task(self , json_data):
    data = json.loads(json_data)
    cur = self.db.cursor()
    sql = "update task set status = 2 where task_id = %s and user_id = '%s'"
    cur.execute(sql % (
      data["task_id"] ,
      data["user_id"]
    ))
    self.db.commit()
    return True