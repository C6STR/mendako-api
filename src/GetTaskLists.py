import Db
import json

class GetTaskList():
    def __init__(self):
        self.db = Db.connect()
    
    def get_task_list(self , json_data):
        cur = self.db.cursor()
        data = json.loads(json_data)

        get_task_list_sql = """
        select task_id , task_name , type , priority , status , DATE_FORMAT(start_daytime , '%%Y/%%m/%%d') , DATE_FORMAT(end_daytime ,'%%Y/%%m/%%d')
        from task 
        where user_id = '%s'
        """

        cur.execute(get_task_list_sql %(
            data["uuid"]
        ))

        rows = cur.fetchall()

        return rows
    
    def get_task_list_date(self, json_data):
        cur = self.db.cursor()
        data = json.loads(json_data)

        get_task_list_sql = """
        select task_id , task_name , type , priority , status , DATE_FORMAT(start_daytime , '%%Y/%%m/%%d') , DATE_FORMAT(end_daytime ,'%%Y/%%m/%%d')
        from task 
        where user_id = '%s' and (status = 0 or status = 1) and end_daytime = '%s'
        """

        cur.execute(get_task_list_sql %(
            data["uuid"],
            data["date"]
        ))

        rows = cur.fetchall()

        return rows