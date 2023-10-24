from flask import Flask, render_template,redirect
from flask_wtf import FlaskForm
from wtforms import StringField,PasswordField,SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.secret_key = "jgkkt5t56565k"
Bootstrap(app)



class LoginForm(FlaskForm):
    email = StringField("Email",validators=[DataRequired()])
    password = PasswordField("Password",validators=[DataRequired()])
    submit = SubmitField("Login")


@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    correct_email = "admin@email.com"
    correct_password = "12345678"
    if form.validate_on_submit():
        if form.email.data == correct_email and form.password.data == correct_password:
            return redirect('/success')
        else:
            return redirect('/denied')

    return render_template('login.html',form=form)

@app.route("/success", methods=['GET'])
def success():
    return render_template('success.html')

@app.route("/denied", methods=['GET'])
def denied():
    return render_template('denied.html')


if __name__ == '__main__':
    app.run(debug=True)