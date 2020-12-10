from flask import Flask, request, render_template
from flask_cors import cross_origin
import sklearn
import pickle
import pandas as pd
import calendar
import numpy as np

app = Flask(__name__)
model = pickle.load(open("linear_regression_model.pkl", "rb"))


@app.route("/")
@cross_origin()
def home():
    return render_template("home.html")


@app.route("/predict", methods=["GET", "POST"])
@cross_origin()
def predict():
    if request.method == "POST":

        # Date_of_Journey
        date_dep = request.form["Dep_Time"]
        DAY_OF_MONTH = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
        MONTH = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").month)
        YEAR = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").year)
        DAY_OF_WEEK = calendar.weekday(YEAR, MONTH, DAY_OF_MONTH)+1
        # print("Journey Date : ",Journey_day, Journey_month)

        # Airline
        # AIR ASIA = 0 (not in column)
        airline = request.form['airline']
        print("airlinsASSAe",airline)
        if (airline == 'Southwest Airline Co. (WN)'):
            AIRLINE_CODE_WN = 1
            AIRLINE_CODE_DL = 0
            AIRLINE_CODE_AS = 0
            AIRLINE_CODE_UA = 0


        elif (airline == 'Delta Air Lines Inc. (DL)'):
            AIRLINE_CODE_WN = 0
            AIRLINE_CODE_DL = 1
            AIRLINE_CODE_AS = 0
            AIRLINE_CODE_UA = 0


        elif (airline == 'Alaskan Airlines Inc. (AS)'):
            AIRLINE_CODE_WN = 0
            AIRLINE_CODE_DL = 0
            AIRLINE_CODE_AS = 1
            AIRLINE_CODE_UA = 0

        elif (airline == 'United Air Lines Inc. (UA)'):
            AIRLINE_CODE_WN = 0
            AIRLINE_CODE_DL = 0
            AIRLINE_CODE_AS = 0
            AIRLINE_CODE_UA = 1

        else:
            AIRLINE_CODE_WN = 0
            AIRLINE_CODE_DL = 0
            AIRLINE_CODE_AS = 0
            AIRLINE_CODE_UA = 0


        Source = request.form["Source"]
        if (Source == '2'):
            ORIGIN_TPA = 1
            ORIGIN_BUR = 0
            ORIGIN_LGA = 0
            ORIGIN_DEN = 0

        elif (Source == '3'):
            ORIGIN_TPA = 0
            ORIGIN_BUR = 1
            ORIGIN_LGA = 0
            ORIGIN_DEN = 0

        elif (Source == '4'):
            ORIGIN_TPA = 0
            ORIGIN_BUR = 0
            ORIGIN_LGA = 1
            ORIGIN_DEN = 0

        elif (Source == '5'):
            ORIGIN_TPA = 0
            ORIGIN_BUR = 0
            ORIGIN_LGA = 0
            ORIGIN_DEN = 1

        else:
            ORIGIN_TPA = 0
            ORIGIN_BUR = 0
            ORIGIN_LGA = 0
            ORIGIN_DEN = 0

        Source = request.form["Destination"]
        if (Source == '2'):
            DESTINATION_ISP = 1
            DESTINATION_SEA = 0
            DESTINATION_CLT = 0
            DESTINATION_JAX = 0
            DESTINATION_TPA = 0

        elif (Source == '3'):
            DESTINATION_ISP = 0
            DESTINATION_SEA = 1
            DESTINATION_CLT = 0
            DESTINATION_JAX = 0
            DESTINATION_TPA = 0

        elif (Source == '4'):
            DESTINATION_ISP = 0
            DESTINATION_SEA = 0
            DESTINATION_CLT = 1
            DESTINATION_JAX = 0
            DESTINATION_TPA = 0

        elif (Source == '5'):
            DESTINATION_ISP = 0
            DESTINATION_SEA = 0
            DESTINATION_CLT = 0
            DESTINATION_JAX = 1
            DESTINATION_TPA = 0

        elif (Source == '6'):
            DESTINATION_ISP = 0
            DESTINATION_SEA = 0
            DESTINATION_CLT = 0
            DESTINATION_JAX = 0
            DESTINATION_TPA = 1

        else:
            DESTINATION_ISP = 0
            DESTINATION_SEA = 0
            DESTINATION_CLT = 0
            DESTINATION_JAX = 0
            DESTINATION_TPA = 0

        print("DESTINATION_ISP",DESTINATION_ISP)

        prediction = model.predict([[
            YEAR,
            MONTH,
            DAY_OF_MONTH,
            DAY_OF_WEEK,
            0,
            0,
            AIRLINE_CODE_DL, #7
            0,
            0,
            0,
            0,
            0,
            0,
            AIRLINE_CODE_UA, #14
            AIRLINE_CODE_WN, #15
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            ORIGIN_BUR, #25
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            ORIGIN_DEN, #35
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            ORIGIN_TPA, #97
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            DESTINATION_CLT, #112
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            DESTINATION_SEA, #171
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            0,
            DESTINATION_TPA,  #180
            0
        ]])

        output = np.exp(prediction[0])
        output_final = round(output, 2)

        return render_template('home.html', prediction_text="Your Flight price is $. {}".format(output_final))

    return render_template("home.html")


if __name__ == "__main__":
    app.run(debug=True)