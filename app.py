from flask import Flask, render_template, request, redirect, url_for, session

# put your code here

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        if validate_user(email, password):
            execute_login(email)

            return redirect(url_for('index'))
        else:
            return render_template('login.html', msg="Nie powiodlo sie try again")

    else:
        if is_user_logged_in():
            return redirect(url_for('index'))
        else:
            return render_template('login.html')


def validate_user(email, password):
    if email == "barrettdomi2@gmail.com" and password == "abd":
        return True
    else:
        return False


def execute_login(user_email):
    session['email'] = user_email


def is_user_logged_in():
    return "email" in session


if __name__ == '__main__':
    app.run(debug=True)
