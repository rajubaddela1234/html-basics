from flask import *

app=Flask(__name__)

@app.route('/login',methods=['GET'])
def login():
    unname=request.args.get('uname')
    password=request.args.get('pass')
    if uname=='ayush' and password=='google':
        return "welcome %s" %uname
    else:
        return "invalid %s" %uname

    if __name__==__main__:
        app.run(debug=True)