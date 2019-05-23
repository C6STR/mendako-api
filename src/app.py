from flask import Flask, jsonify,request
import GetTaskLists
import GetTask
import PutTask
import json

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

@app.route("/put-task" , methods = ['POST'])
def index_1():
  putter = PutTask.PutTask()
  data = request.data.decode('utf-8')
  putter.put_task(data)
  data = json.loads(data)
  return jsonify(data)

#こんなもんはいらん
@app.route("/mysql")
def mysql():
  pass
  #db = TestDbConnect.DbTest()
  #rows = db.get()
  #return jsonify(rows)

##テスト用
@app.route("/test-post")
def test_post():
  print(request.json)

#if __name__ == '__main__':
#  app.run()
