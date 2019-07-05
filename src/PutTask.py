import Db
import json

class PutTask():
    def __init__(self):
        self.db = Db.connect()

    def put_task(self , json1):
        cur = self.db.cursor()
        data = json.loads(json1)
        created_daytime = "2019-1-1"
        sql = """
            insert into `task`(
                user_id ,
                task_name ,
                type ,
                priority ,
                start_daytime ,
                end_daytime ,
                created_daytime ,
                updated_daytime,
            )values(
                '%s',
                '%s',
                %s,
                %s,
                '%s',
                '%s',
                '%s' ,
                '%s'
            )
        """
        cur.execute(sql %(
            data["user_id"] ,
            data["task_name"] ,
            data["types"] ,
            data["priority"] ,
            data["start_daytime"] ,
            data["end_daytime"] ,
            created_daytime ,
            created_daytime
        ))
        self.db.commit()