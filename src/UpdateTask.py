import Db
import json

class UpdateTask():
  def __init__(self):
    self.db = Db.connect()
  
  def update_task(self, json_data):
    cur = self.db.cursor()
    data = json.loads(json_data)
    print(data)

    sql = """
      update `task` set
        task_name = '%s',
        type = %s,
        priority = %s,
        status = %s,
        start_daytime = '%s',
        end_daytime = '%s'
      where
        task_id = %s
    """

    cur.execute(sql %(
      data["task"]["task_name"],
      data["task"]["type"],
      data["task"]["priority"],
      data["task"]["status"],
      data["task"]["start_daytime"],
      data["task"]["end_daytime"],
      data["task"]["task_id"]
    ))

    self.db.commit()