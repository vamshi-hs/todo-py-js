from flask_cors import CORS
from flask import Flask,jsonify,request
import sqlite3

app = Flask(__name__)
CORS(app)

#Connect to database
def get_db_connection():
    conn = sqlite3.connect('database.db')
    print("Connected to database succesfully")

    conn.execute('CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY AUTOINCREMENT, task TEXT, status TEXT)')
    print("Created table successfully")

    return conn

def get_status(status):
    if status == "incomplete":
        return False
    elif status == "completed":
        return True

def post_status(status):
    if status == False:
        return "incomplete"
    elif status == True:
        return "completed"

@app.route("/todos")
def list_todos():
    conn = get_db_connection()
    result = conn.execute('SELECT * from tasks')
    tasks = result.fetchall()
    conn.close()
    response = my_jsonify(tasks)
    response.status_code = 200
    return response

@app.route("/todos",methods=["POST","GET"])
def post_one_todo_and_view():
    if request.method == 'POST':
        data = request.json
        conn = get_db_connection()
        conn.execute('INSERT INTO tasks(task,status) VALUES(?,?)'
                     ,(data,post_status(False)))
        conn.commit()
        conn.close()
    response = list_todos()
    return response


@app.route("/todos",methods=["DELETE","GET"])
def delete_one_todo_and_view():
    if request.method == 'DELETE':
        data = request.json
        conn = get_db_connection()
        conn.execute('DELETE FROM tasks WHERE id=(? )'
                     ,[int(data)])
        conn.commit()
        conn.close()
    response = list_todos()
    return response

def my_jsonify(data):
    my_json = map (lambda x:{
        'id':x[0],
        'task':x[1],
        'status':get_status(x[2])
    },data
    )
    return (jsonify(list(my_json)))

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0',)
