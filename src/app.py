from flask import Flask, jsonify,request
import json
from flask_cors import CORS

import GetTaskLists
import GetTask
import PutTask
import DoneTask
import UserRegister
import UserLogin
import UserAuthToken

import logging

app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)
CORS(app)
app.config['JSON_AS_ASCII'] = False

@app.route('/')
def index():
  app.logger.error('error')
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

#タスク完了
@app.route("/done-task" , methods = ['POST'])
def done_task():
  updater = DoneTask.DoneTask()
  data = request.data.decode('utf-8')
  res = updater.done_task(data)
  return jsonify(res)

## ユーザー管理
# ユーザー登録
@app.route("/user-register" , methods = ['POST'])
def user_register():
  ur = UserRegister.UserRegister()
  data = request.data.decode('utf-8')
  ur.user_register(data)
  return("ok")

# ユーザーログイン
@app.route("/user-login" , methods = ['post'])
def user_login():
  ul = UserLogin.UserLogin()
  data = request.data.decode('utf-8')
  res = ul.user_login(data)
  return jsonify(res)

# トークン確認
@app.route("/user-checktoken" , methods = ['post'])
def user_checktoken():
  uat = UserAuthToken.UserAuthToken()
  data = request.data.decode('utf-8')
  res = uat.user_auth_token(data)
  ret = {"status" : res}
  return ret