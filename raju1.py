from flask import Flask

app=Flask(__name__)

def kiran():
    return 'this is raju'

app.add_url_rule('/kiran','kiran',kiran)


if __name__=='__main__':
    app.run(debug=True)