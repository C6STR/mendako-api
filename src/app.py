from flask import Flask, jsonify
import GetTaskLists
import TestDbConnect
import GetTask
import PutTask

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
  return jsonify({
    "message": "テスト!!"
  })

@app.route("/get-task")
def get_task():
  getter = GetTask.GetTask()
  json = getter.get_task()
  return jsonify(json)

@app.route("/put-task")
def put_task():
  put_task = PutTask.PutTask()

@app.route("/mysql")
def mysql():
  db = TestDbConnect.DbTest()
  rows = db.get()
  return jsonify(rows)

if __name__ == '__main__':
  app.run()
