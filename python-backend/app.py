from flask_cors import CORS
from flask import Flask,jsonify,request
# import sqlite3

app = Flask(__name__)
CORS(app)

todos = ["emacs","xmonad","haskell"]

@app.route("/todos")
def list_todos():
    return my_jsonify(todos) 

@app.route("/todos",methods=["POST","GET"])
def post_todo_and_view():
    if request.method == 'POST':
        data = request.json
        todos.append(data)
    return list_todos()

def my_jsonify(data):
    my_json = map (lambda x:{'task':x
    },data
    )
    return (jsonify(list(my_json)))

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',)
