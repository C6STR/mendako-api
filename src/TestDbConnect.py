import Db
class DbTest():
    def __init__(self):
        self.db = Db.connect()
    
    def get(self):
        cur = self.db.cursor()
        sql = "select * from test"
        cur.execute(sql)
        rows = cur.fetchall()
        print(rows)

if __name__ == "__main__":
    dbtest = DbTest()
    dbtest.get()