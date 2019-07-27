import PutTask
import json

pt = PutTask.PutTask()

data = {
    "user_id" : "user_id_001",
    "task_name" : "タスク名" ,
    "type" : 1,
    "priority" : 1,
    "start_daytime" : "2019-1-1",
    "end_daytime": "2019-1-2"
}
json = json.dumps(data)

pt.put_task(json)