from flask import Flask, jsonify
import GetTaskLists

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
  return jsonify({
    "message": "テスト!!"
  })

@app.route("/get-task")
def tako():
  getter = GetTaskLists.GetTaskList()
  json = getter.get_task_list()
  return jsonify(json)

if __name__ == '__main__':
  app.run()
