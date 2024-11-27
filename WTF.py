from form import LoginForm
from flask import Flask, request, render_template, flash
import email_validator

app = Flask(__name__)
app.config['SECRET_KEY'] = "PAVAN"

@app.route("/")
def home():
    return "Welcome buddy!"

@app.route("/lo", methods=["POST", "GET"])
def home1():
    form = LoginForm()
    if request.method == "POST":
        print("Form submitted")  # Debugging
        if not form.validate():
            print("Validation failed")  # Debugging
            flash("ENTER ALL THE DETAILS")
            return render_template("contact.html", form=form)
        else:
            print("Validation succeeded")  # Debugging
            return "SUCCESSFULLY LOGGED IN"
    print("GET request")  # Debugging
    return render_template("contact.html", form=form)
if __name__ == "__main__":
    app.run(debug=True)
