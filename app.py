from flask import Flask, render_template, request
from datetime import datetime
import re
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/', methods = ['POST'])
def gettime():
    date = datetime.strptime(request.form['datetime'], '%Y-%m-%dT%H:%M')
    return render_template('index.html', timestamp="<br>Paste this code into discord for<br>a multi-timezone timestamp: &lt;t:" + str(datetime.timestamp(date)).split('.', 1)[0] + "&gt;")
if __name__ == "__main__":
  app.run()