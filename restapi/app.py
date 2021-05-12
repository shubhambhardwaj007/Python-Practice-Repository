from flask import Flask,request,render_template
app=Flask("myiiec")
@app.route("/form")
def myform():
    return render_template("basic.html")

@app.route("/data",methods=['POST'])
def mydata():
    if request.method=="POST":
        data=request.form.get("x")
        print(data)
    return "data"
@app.route("/name")
def myname():
    return "vimsl"

app.run(port=5555,debug=True)
