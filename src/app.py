from flask import Flask, jsonify,request
import json
from flask_cors import CORS

import GetTaskLists
import GetTask
import PutTask
import UserRegister

app = Flask(__name__)
CORS(app)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
  return jsonify({
    "message": "テスト!!"
  })

## タスク管理
# タスク取得
@app.route("/get-task")
def get_task():
  getter = GetTask.GetTask()
  json = getter.get_task()
  return jsonify(json)

# タスク登録
@app.route("/put-task" , methods = ['POST'])
def put_task():
  putter = PutTask.PutTask()
  data = request.data.decode('utf-8')
  putter.put_task(data)
  data = json.loads(data)
  return jsonify(data)

# タスク一覧取得
@app.route("/get-tasklist" , methods = ['POST'])
def get_tasklist():
  getter = GetTaskLists.GetTaskList()
  data = request.data.decode('utf-8')
  res = getter.get_task_list(data)
  return jsonify(res)

## ユーザー管理
# ユーザー登録
@app.route("/user-register" , methods = ['POST'])
def user_register():
  ur = UserRegister.UserRegister()
  data = request.data.decode('utf-8')
  ur.user_register(data)
  return("ok")


#
##こんなもんはいらん
#@app.route("/mysql")
#def mysql():
#  pass
#  #db = TestDbConnect.DbTest()
#  #rows = db.get()
#  #return jsonify(rows)
#
###テスト用
#@app.route("/test-post")
#def test_post():
#  print(request.json)
#
##if __name__ == '__main__':
##  app.run()
