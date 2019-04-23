from flask import Flask, render_template, request
from github import Github
import requests


app=Flask(__name__)
@app.route('/github', methods=['post'])
def index():
    username = request.form['user']
    r = requests.get('http://api.github.com/repositories?q=user:username,us&accesstoken=fd7a0584744659f660c88d0ce3306362c3e9d9e6')
    for repo in r:
      return r
@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)
