from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def hello():
  return 'hello world!'

@app.route("/day_hour_heatmap")
def day_hour_heatmap():
  return render_template('day_hour_heatmap/index.html')

if __name__ == "__main__":
  app.run()