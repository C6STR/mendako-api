import PutTask
import json

pt = PutTask.PutTask()

data = {
    "user_id" : "c5dada86-dad7-43ee-a802-5021d9fbb1ad",
    "task_name" : "タスク名2334" ,
    "type" : 1,
    "priority" : 1,
    "start_daytime" : "2019-1-1",
    "end_daytime": "2019-1-2"
}
json = json.dumps(data)

pt.put_task(json)