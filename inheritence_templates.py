from flask import Flask ,render_template
app=Flask(__name__)
@app.route("/")
def home2():
    return render_template("inheritence_base.html")
@app.route("/inherited_base")
def home3():
    return render_template("inherited_base.html")
@app.route("/inherited2")
def home4():
    return render_template("inherited2.html")
if __name__ == "__main__":
    app.run(debug=True)