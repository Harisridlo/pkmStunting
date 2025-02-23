from flask import Flask, request, render_template, redirect, url_for

app = Flask( __name__)

acc = {"admin":"1234",
       "mina":"tobrut"}

@app.route("/")
def haha():
    return render_template("login.html")

@app.route("/login", methods = ['POST', 'GET'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    if username in acc and acc[username]==password:
        return render_template('index.html')
    else:
        return redirect('/login')
    
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/register')
def register():
    return render_template('register.html')



if __name__ == "__main__":
    app.run(debug=True)
