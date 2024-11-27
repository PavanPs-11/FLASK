from flask import Flask ,render_template
app=Flask(__name__)
@app.route("/templates")
def home2():
    return render_template("index.html",content=["ML","DJANGO","SQL","PYTHON"])
@app.route("/")
def home():
    return render_template("home.html")
if __name__ == "__main__":
    app.run(debug=True)
