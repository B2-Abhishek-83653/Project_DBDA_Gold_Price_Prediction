#!/bin/python

from flask import Flask,render_template, url_for, request
import numpy as np
from joblib import Parallel, delayed 
import joblib
import pickle
from datetime import datetime

# Flask function has variable __name__which tells flask all functions and variable can be inherited from ./flask_installed
app = Flask(__name__)

#Python decorator for route of website id current directory
@app.route("/")
#@app.route("/home")


#@app.route("/visualisation.html")

def home():
    return render_template("index.html")


# prediction function
def ValuePredictor(to_predict_list):
	#to_predict = np.array(to_predict_list).reshape(1, 12)
    to_predict = np.array(to_predict_list).reshape(1, -1)
    #loaded_model = pickle.load(open("./pr_model.pkl", "rb"))
    loaded_model = joblib.load('static/models/svr_model.pkl') 
    result = loaded_model.predict(to_predict)
    
    # # get the predicted data
    # y_pred = loaded_model.predict(x_test)
    # # getting the true values
    # y_true = y_test
    # from sklearn.metrics import mean_absolute_error

    # mae = mean_absolute_error(y_true, y_pred)

    # from sklearn.metrics import mean_squared_error
    # mse = mean_squared_error(y_true, y_pred)

    # from sklearn.metrics import root_mean_squared_error

    # rmse = root_mean_squared_error(y_true, y_pred)
    # from sklearn.metrics import r2_score
    # r2 = r2_score(y_true, y_pred)
    return result[0]

@app.route('/result', methods = ['POST'])
def result():
    if request.method == 'POST':
        my_input=request.form.to_dict()
        to_predict_list = my_input
        to_predict_list = list(to_predict_list.values())
        #to_predict_list = list(map(int, to_predict_list))
        # result = ValuePredictor(to_predict_list)
        # return render_template("result.html", prediction = f"At date {to_predict_list}, Gold value is ${result}")


        #format_string = "%Y-%m-%d"
        #datetime_object = datetime.strptime(to_predict_list[0], format_string)
        #my_num = datetime_object.strftime("%y")+datetime_object.strftime("%m")+datetime_object.strftime("%d")
        #to_predict_list = list(map(int, my_num))
        
        to_predict_list = my_input['date'][2:4] + my_input['date'][3:4] + my_input['date'][:3]

        



        result = ValuePredictor(int(to_predict_list))
        #return render_template("result.html", prediction = f"At date {my_input['date']}, Gold value is ${result}\n ACcuracy is {r2*100}%")
        return render_template("result.html", prediction = f"At date {my_input['date']}, Gold value is ${result}")



if __name__ == "__main__":
    #app.run(debug=True)
    app.run(debug=True,host="0.0.0.0",port=8002)



# @app.route('/result',methods=['POST', 'GET'])
# def result():
#     output = request.form.to_dict()
#     print(output)
#     name = output["name"]


#     return render_template('index.html', name = name)



# def index():
#     return "test"


# # run on localhost
#app.run(host="0.0.0.0",port=8002)
# # if permission denied change port number
