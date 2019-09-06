import GetTaskLists
import json

gt = GetTaskLists.GetTaskList()

data = {
    "uuid" : "c5dada86-dad7-43ee-a802-5021d9fbb1ad",
}
json = json.dumps(data)

rows = gt.get_task_list(json)
print(rows)