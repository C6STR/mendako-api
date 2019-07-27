import Db
import json

class PutTask():
    def __init__(self):
        self.db = Db.connect()

    def put_task(self , data):
        cur = self.db.cursor()
        data = json.loads(data)
        sql = """
            insert into `task`(
                user_id ,
                task_name ,
                type,
                priority ,
                start_daytime ,
                end_daytime
            )values(
                '%s',
                '%s',
                %s,
                %s,
                '%s',
                '%s'
            )
        """
        cur.execute(sql %(
            data["user_id"] ,
            data["task_name"] ,
            data["type"] ,
            data["priority"] ,
            data["start_daytime"] ,
            data["end_daytime"] ,
        ))
        self.db.commit()