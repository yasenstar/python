from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    # return "Yasen Info Harbor"
    bmi = 0.0
    if request.method == 'POST':
        w = float(request.form['weight'])
        h = float(request.form['height'])
        bmi = w / (h ** 2)
    return render_template("index.html", bmi=round(bmi,1))