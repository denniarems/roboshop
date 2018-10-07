from flask import Flask, render_template, request
from data import robodata
app = Flask(__name__)

getrobolist = robodata()


@app.route('/')
@app.route('/home')
def index():
    return render_template('home.html', bot=getrobolist)


@app.route('/shop')
def shop():
    return render_template('shop.html', bot=getrobolist)


@app.route('/contact')
def contact():
    return render_template('contact.html')


@app.route('/buy', methods=['GET', 'POST'])
def buy():
    if(request.method == 'POST'):
        readName = request.form['name']
        readRobot = request.form['robo']
        return render_template('recipt.html', myname=readName, myrobot=readRobot)


@app.route('/feedback', methods=['GET', 'POST'])
def feed():
    if(request.method == 'POST'):
        readName = request.form['name']
        readEmail = request.form['email']
        return render_template('feedback.html', myname=readName, myemail=readEmail)


if __name__ == '__main__':
    app.run()
