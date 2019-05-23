import sys,os

sys.path.append(os.pardir)
import Db

args = sys.argv
class SeedTestTask():

    def create_seed(self):
        self.seed = []

        self.seed.append({
            "task-name" : "買い物",
            "type" : 1 ,
            "priority" : 1 ,
            "status" : 1 ,
            "start-daytime" : "2019-1-1" ,
            "end-daytime" : "2019-1-2"
            })

        self.seed.append({
            "task-name" : "買い物2",
            "type" : 1 ,
            "priority" : 1 ,
            "status" : 1 ,
            "start-daytime" : "2019-2-1" ,
            "end-daytime" : "2019-2-2"
        }
        )

    def insert(self , data):
        db = Db.connect()
        cur = db.cursor()

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
            data["type"] ,
            data["priority"] ,
            data["status"] ,
            data["start-daytime"] ,
            data["end-daytime"] ,
        ))
        db.commit()

    def setup(self):
        for data in self.seed:
            self.insert(data)

    def teardown(self):
        pass

if __name__ == "__main__":
    test = SeedTestTask()
    test.create_seed()
    
    test.setup()
    #test.teardown()
