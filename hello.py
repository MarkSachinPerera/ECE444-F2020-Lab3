from flask import Flask, render_template, session, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from datetime import datetime
from forms import submitForm

app = Flask(__name__)
app.config['SECRET_KEY'] = "LOLLOL"
bootstrap = Bootstrap(app)
moment = Moment(app)

@app.route('/', methods=['POST','GET'])
@app.route('/index', methods=['POST', 'GET'])
def index():
    form = submitForm()
    if form.validate_on_submit():
        session['name'] = form.name.data
        session['email'] = form.email.data
        return redirect(url_for('index'))    
    return render_template('index.html', current_time=datetime.utcnow(), form=form, name=session.get('name'), email=session.get('email'))
    

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name, current_time=datetime.utcnow())


if __name__ == '__main__':
    app.run(debug=True)