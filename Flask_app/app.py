from Flask import Flask
app=flask()

@app.route("/search")
def mysearch():
    print("SEARCH...........")
@app.route("/email")
def myemail():
    print("EMAIL.........")
