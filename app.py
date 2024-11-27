from flask import Flask ,redirect,url_for
app=Flask(__name__)
@app.route("/")
def hello():
    return "<h1> welcome to flask</h1>"
@app.route("/skills")
def skills():
    list1=["python","flask","django"]
    return [i for i in list1]
@app.route("/<dynamicrouting>")
def name(dynamicrouting):
    return f"HELLO  {dynamicrouting} "
@app.route("/admin")
def home2():
    return redirect(url_for('skills'))
if __name__ == "__main__":
    app.run(debug=True)