from flask import Flask, render_template, url_for, redirect, request, session
from datetime import timedelta
app = Flask(__name__)
app.secret_key = "PAVAN"
app.permanent_session_lifetime=timedelta(seconds=5)

@app.route("/")
def home():
    return render_template("form1.html")

@app.route("/login", methods=["POST", "GET"])
def home2():
    if request.method == "POST":
        session.permanent=True
        user = request.form["usr_name"]
        session["user"] = user
        return redirect(url_for("home"))
    else:
        if "user" in session:
            return redirect(url_for("home3"))
    return render_template("login.html")

@app.route("/user")
def home3():
    if "user" in session:  # Fixed the space issue
        user = session["user"]
        return f"Hello {user} ❤️❤️❤️❤️❤️❤️❤️❤️"
    else:
        return redirect(url_for("home2"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("home2"))

if __name__ == "__main__":
    app.run(debug=True)
