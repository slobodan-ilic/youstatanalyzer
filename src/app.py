from flask import Flask, make_response, request
from statistics import analyze_stats
import json


app = Flask(__name__)


@app.route('/')
def index():
    return make_response(open("templates/index.html").read())


@app.route('/stats.json')
def fetch_stats():
    video_id = request.args.get('vid', None)
    statistics = analyze_stats(video_id)
    if statistics is not None:
        print "keys: ", statistics.keys()
        return json.dumps(statistics)
    else:
        return "Could not fetch data."


if __name__ == "__main__":
    app.run(debug=True)
