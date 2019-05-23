import Db
class GetTask():
    def __init__(self):
        self.db = Db.connect()
    
    def get_task(self):
        cur = self.db.cursor()
        sql = "select * from `test-task`"
        cur.execute(sql)
        rows = cur.fetchall()
        return rows