from flask import Flask, session

from check_logged_in import check_logged_in

app = Flask(__name__)

@app.route('/')
def hello() -> str:
    return 'Hello from the simple webapp'

@check_logged_in
@app.route('/page1')
def page1():
    return 'This is page 1'

@check_logged_in
@app.route('/page1')
def page2():
    return 'This is page 2'

@check_logged_in
@app.route('/page1')
def page3():
    return 'This is page 3'

@app.route('/logout')
def do_logout() -> str:
    session.pop('logged_in')
    return 'You are now logged out'

@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in.'


app.secret_key = 'YouWillNeverGuessMySecretKey'


if __name__ == '__main__':
    app.run(debug=True)
