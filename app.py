from flask import Flask, render_template, request
from data import departures, tours

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


@app.route('/departures/<key>')
def departure(key):
    return render_template('departure.html', deps=departures, key=key, tours=tours)


@app.route('/tours/<int:tour_id>')
def tour(tour_id):
    return render_template('tour.html', tour=tours[tour_id], dep=departures[tours[tour_id]['departure']])


if __name__ == '__main__':
    app.run()
