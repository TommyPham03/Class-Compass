from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # TODO: Authenticate user credentials here

        return redirect(url_for('schedule'))

    return render_template('login.html')


@app.route('/schedule')
def schedule():
    # TODO: Retrieve user schedule data and render schedule template
    return render_template('schedule.html')


if __name__ == '__main__':
    app.run(debug=True)