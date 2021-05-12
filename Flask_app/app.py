from  flask import Flask,render_template
import subprocess
app = Flask("myapp")

@app.route("/")
def mysearch():
    print("I AM IN HOME DIR")
    return("I AM IN HOME DIR")
@app.route("/menu",methods=["GET"])
def mymenu():
    name=request.args.get("x")
    #html_code = render_template("mymenu.html", name= "dynamic_name",cname="dynamic_cname")
    print(x)
    return x
@app.route("/form")
def myform():
    print("MY PAGE : form page")
    form_html_code = render_template("form.html")
    return form_html_code
