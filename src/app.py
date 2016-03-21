from flask import Flask
from statistics import analyze_stats


app = Flask(__name__)


@app.route("/")
def index():
    statistics = analyze_stats('4ap0k6ZBqgQ')
    return str(statistics)

if __name__ == "__main__":
    app.run(debug=True)
