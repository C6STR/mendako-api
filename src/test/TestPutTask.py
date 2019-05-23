import PutTask
import json

pt = PutTask.PutTask()

data = {
    "task-name" : "インサートするタスク" ,
    "type" : 1,
    "priority" : 1,
    "status" : 1,
    "start-daytime" : "2019-1-1",
    "end-daytime": "2019-1-2"
}
json = json.dumps(data)

pt.put_task(json)