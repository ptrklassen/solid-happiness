from flask import Flask
from flask import render_template

app = Flask(__name__)

JOBS = [
  {
    "id": 1,
    "title": "Data Analyst",
    "location": "Calgary, AB",
    "salary": "$65,000"
  },
  {
    "id": 2,
    "title": "Data Scientist",
    "location": "Edmonton, AB",
    "salary": "$85,000"
  },
  {
    "id": 3,
    "title": "Web Developer",
    "location": "Edmonton, AB",
  },
  {
    "id": 4,
    "title": "Back End Engineer",
    "location": "Calgary, AB",
    "salary": "$115,000"
  },
]


@app.route("/")
def hello_world():
  return render_template("home.html", jobs=JOBS)


if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
