import mysql.connector
from flask import Flask, render_template, request

app = Flask(__name__)

# MySQL configuration
app.config['MYSQL_HOST'] = 'localhost'  # MySQL server
app.config['MYSQL_USER'] = 'root'  # MySQL username
app.config['MYSQL_PASSWORD'] = 'Ksiddu0575@'  # MySQL password
app.config['MYSQL_DB'] = 'flask_pro'  # MySQL database name

# Initialize MySQL
mysql = mysql.connector.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    database=app.config['MYSQL_DB']
)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            weight = float(request.form["weight"])
            height = float(request.form["height"])
            bmi = weight / (height ** 2)
            category = ""

            if bmi < 18.5:
                category = "Underweight"
            elif 18.5 <= bmi < 24.9:
                category = "Normal weight"
            elif 25 <= bmi < 29.9:
                category = "Overweight"
            else:
                category = "Obesity"

            # Store the data in MySQL
            cursor = mysql.cursor()
            cursor.execute("INSERT INTO bmi_records (weight, height, bmi, category) VALUES (%s, %s, %s, %s)", 
                           (weight, height, bmi, category))
            mysql.commit()

            return render_template("index1.html", bmi=bmi, category=category)
        except ValueError:
            return render_template("index1.html", error="Please enter valid numbers for weight and height.")
    return render_template("index1.html")

if __name__ == "__main__":
    app.run(debug=True)
