import PutTask
import json

pt = PutTask.PutTask()

data = {
    "user_id" : "user_id_001",
    "task-name" : "タスク名" ,
    "types" : 1,
    "priority" : 1,
    "start-daytime" : "2019-1-1",
    "end-daytime": "2019-1-2"
}
json = json.dumps(data)

pt.put_task(json)