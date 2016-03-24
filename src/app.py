from flask import Flask, make_response, request, send_file
from statistics import analyze_stats, generate_spreadsheet
import json
import os
import StringIO
from flask import make_response


app = Flask(__name__)
s = None
mimetype = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'


@app.route('/')
def index():
    # Using make_response instead of render_template, because of AngularJS.
    return make_response(open("templates/index.html").read())


@app.route('/stats.json')
def stats():
    video_id = request.args.get('vid', None)
    statistics = analyze_stats(video_id)
    if statistics is not None:
        global s
        s = statistics
        return json.dumps(s)
    else:
        return "Could not fetch data."


@app.route('/statistics_spreadsheet')
def statistics_spreadsheet():
    global s
    if os.name == 'posix':
        filename = '/tmp/statistics.xlsx'
    elif os.name == 'nt':
        filename = os.getcwd() + '\\' + 'statistics.xlsx'
    generate_spreadsheet(s, filename)
    return send_file(filename, add_etags=False)
    # output = generate_spreadsheet(s)
    # output.seek(0)
    # return send_file(output, mimetype=mimetype, cache_timeout=0)

if __name__ == "__main__":
    app.run(debug=True)
