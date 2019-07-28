import Db
import json

class GetTaskList():
    def __init__(self):
        self.db = Db.connect()
    
    def get_task_list(self , json_data):
        cur = self.db.cursor()
        data = json.loads(json_data)

        get_task_list_sql = """
        select task_name , type , priority , status , start_daytime , end_daytime 
        from task 
        where user_id = '%s'
        """

        cur.execute(get_task_list_sql %(
            data["uuid"]
        ))

        rows = cur.fetchall()

        return rows