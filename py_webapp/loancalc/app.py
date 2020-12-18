from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET","POST"])
def home():
    monthlypayment = 0.0
    
    return render_template("index.html", monthlypayment=round(monthlypayment,1))