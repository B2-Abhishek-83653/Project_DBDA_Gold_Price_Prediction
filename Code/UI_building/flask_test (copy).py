#!/bin/python

from flask import Flask,render_template, url_for, request


# Flask function has variable __name__which tells flask all functions and variable can be inherited from ./flask_installed
app = Flask(__name__)

#Python decorator for route of website id current directory
@app.route("/")
@app.route("/home")


def home():
    return render_template("index.html")

@app.route('/button',methods=['POST', 'GET'])
def button():
    output2 = request.form.to_dict()
    print(output2)
    name = output2["name"]


    return render_template('index.html', name = name)
    


@app.route('/result',methods=['POST', 'GET'])
def result():
    output = request.form.to_dict()
    print(output)
    name = output["name"]


    return render_template('index.html', name = name)



if __name__ == "__main__":
    #app.run(debug=True)
    app.run(debug=True,host="0.0.0.0",port=8002)




# def index():
#     return "test"


# # run on localhost
#app.run(host="0.0.0.0",port=8002)
# # if permission denied change port number