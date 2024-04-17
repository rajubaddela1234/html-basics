from flask import Flask

app=Flask(__name__)


@app.route('/hello/<name>')
def kiran(name):
    return  'I LOVE YOU'+name


if __name__=='__main__':
    app.run(debug=True)