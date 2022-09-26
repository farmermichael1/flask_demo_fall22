#app.py

from flask import Flask, render_template, request
app = Flask(__name__)

todoList = []

@app.route("/")
def hello():
    return render_template('home.html')

@app.route('/addTodo', methods=['POST'])
def addTodo():
    todoItem = request.form['text1']
    todoList.append(todoItem)
    return render_template('home.html', todoList=todoList)


if __name__ == "__main__":
    app.run(debug=True)



