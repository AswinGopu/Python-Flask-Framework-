
from flask import Flask,redirect,url_for,request
app=Flask(__name__)
@app.route("/")
def index():
    return "<h1 style=color:red>welcome</h1>"
@app.route("/home",methods=["GET","POST"]) 
def home():
    if request.method =='GET':
            uname=request.args.get("uname")
            passd=request.args.get("pwd")
            return "<h1 style=color:green>welcome %s</h1>"%uname
    else:
        uname=request.form["uname"]
        passd=request.form["pwd"]
        return "<h1 style=color:green>hi %s</h1>"%uname
app.run(debug=True) 