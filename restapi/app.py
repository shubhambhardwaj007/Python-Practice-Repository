from flask import Flask,request,render_template
app=Flask("myiiec")
@app.route("/form")
def myform():
    return render_template("basic.html")

@app.route("/data",methods=['GET'])
def mydata():
    if request.method=="GET":
        data=request.args.get("x")
        print(data)
    return "data"

app.run(port=5555,debug=True)
