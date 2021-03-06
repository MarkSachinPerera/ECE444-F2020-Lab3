from flask import Flask, render_template, session, redirect, url_for, flash
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from forms import submitForm
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = "LOLLOL"
bootstrap = Bootstrap(app)
moment = Moment(app)

uoftemail = re.compile('.*(utoronto.ca)')


@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
def index():
    form = submitForm()
    if form.validate_on_submit():
        old_name = session.get('name')
        old_email = session.get('email')

        if old_name is not None and form.name.data != old_name:
            flash("Looks like you changed your name!")
        if old_email is not None and old_email != form.email.data:
            flash("Looks like you changed your email!")

        session['name'] = form.name.data

        if uoftemail.match(form.email.data):
            session['email'] = form.email.data
        else:
            session['email'] = None

        return redirect(url_for('index'))
    return render_template('index.html', current_time=datetime.utcnow(), form=form, name=session.get('name'), email=session.get('email'))


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name, current_time=datetime.utcnow())


if __name__ == '__main__':
    app.run(debug=True)
