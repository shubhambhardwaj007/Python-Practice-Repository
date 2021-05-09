from  flask import Flask,render_template
import subprocess
app = Flask("myapp")

@app.route("/")
def mysearch():
    print("I AM IN HOME DIR")
    return("I AM IN HOME DIR")
@app.route("/menu")
def mymenu():
    print("MY PAGE : menu page")
    html_code = render_template("mymenu.html", name= "dynamic_name",cname="dynamic_cname")
    return html_code
