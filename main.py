from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/api/v1/<station>/<date>')
def about(station, date):
    temparature = 23
    return {'station': station,
            'date': date,
            'temparature': temparature}


if __name__ == "__main__":
    app.run(debug=True)