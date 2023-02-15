from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = 'secret'
Bootstrap(app)

class MyForm(FlaskForm):
    email = StringField(label='email', validators=[DataRequired(), Email(message='not valid email')])
    password = PasswordField(label='password', validators=[DataRequired(), Length(min=8, max=30,
                                                                                message='Password min 8 and max30')])
    submit = SubmitField(label='Log in')

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = MyForm()
    if form.validate_on_submit():
        if form.password.data == '12345678' and form.email.data == 'admin@email.com':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=form)


@app.route("/register", methods=['GET', 'POST'])
def register_page():
    return 'register'

if __name__ == '__main__':
    app.run(debug=True)