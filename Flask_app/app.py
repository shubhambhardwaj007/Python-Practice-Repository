from  flask import Flask,render_template
import os
import subprocess
app = Flask("iiec-rise")

@app.route("/search")
def mysearch():
    data=subprocess.getoutput("date /t")
    print("MY PAGE : SEARCH...........")
    print(data)
    return(data)
@app.route("/email")
def myemail():
    print("MY PAGE : EMAIL.........")
    return render_template("email.html")
