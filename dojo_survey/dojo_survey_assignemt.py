from flask import Flask, session, request, redirect, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    

@app.route('/results', methods=['POST'])
def process():
    name = request.form['student_name']
    location = request.form['hideout_location']
    weapon = request.form['fav_weap']
    comment = request.form['say_it']
    return render_template('results.html', name=name, location=location, weapon= weapon, comment=comment)

app.run(debug=True)