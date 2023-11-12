# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 17:52:24 2023

@author: Admin
"""

from flask import Flask,render_template,request
import pickle
#import pandas as pd
#import numpy as np

model=pickle.load(open('predictor.pkl','rb'))
#scalar=pickle.load(open('scaler.pkl','rb'))

app= Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/pred',methods=['POST']) # prediction route
def predict1():
    '''
    For rendering results on HTML 
    '''
    
    ym = request.form["yummy"]
    cn = request.form["convenient"]
    sp = request.form["spicy"]
    fl = request.form["flattening"]
    gr = request.form["greasy"]
    fs = request.form["fast"]
    ch = request.form["cheap"]
    ts = request.form["tasty"]
    ex = request.form["expensive"]
    he = request.form["healthy"]
    ds = request.form["disgusting"]
    lk = request.form["Like"]
    a = request.form["Age"]
    vf = request.form["VisitFrequency"]
    g = request.form["Gender"]
    t =  [[ym,cn,sp,fl,gr,fs,ch,ts,ex,he,ds,lk,a,vf,g]]
    #x=scalar.transform(t)
    output =model.predict(x)
    print(output)
    
    
    return render_template("index.html", result = "The predicted cluster is "+str(np.round(output[0])))

if __name__ == "__main__":
    app.run()