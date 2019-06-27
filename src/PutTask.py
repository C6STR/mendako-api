import Db
import json

class PutTask():
    def __init__(self):
        self.db = Db.connect()

    def put_task(self , json1):
        cur = self.db.cursor()
        data = json.loads(json1)
        sql = """
            insert into `test-task`(
                `task-name` ,
                types ,
                priority ,
                status ,
                `start-daytime` ,
                `end-daytime`
            )values(
                '%s',
                %s,
                %s,
                %s,
                '%s',
                '%s'
            )
        """
        cur.execute(sql %(
            data["task-name"] ,
            data["types"] ,
            data["priority"] ,
            data["status"] ,
            data["start-daytime"] ,
            data["end-daytime"] ,
        ))
        self.db.commit()