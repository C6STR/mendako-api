class GetTaskList():
    def __init__(self):
        pass
    
    def get_task_list(self):
        #これはよくない
        json_sample = {
            "task-id":1,
            "task-name":"たすくてすと",
            "type":"memo",
            "priority":"high",
            "status":"Doing",
            "start-daytime":"2019-01-12",
            "start-daytime":"2019-01-15",
            "child-task-id":2
        }
        return json_sample