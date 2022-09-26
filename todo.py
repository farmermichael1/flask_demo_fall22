#app.py

from flask import Flask, render_template, request
app = Flask(__name__)



@app.route("/")
def hello():
    return render_template('home.html')

@app.route('/addTodo', methods=['POST'])
def addTodo():
    text1 = request.form['text1']
    print(text1)
    return(text1)


if __name__ == "__main__":
    app.run(debug=True)



