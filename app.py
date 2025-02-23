from flask import Flask, render_template, request, redirect,session,url_for 
import mysql.connector
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

db = mysql.connector.connect(
    host="localhost",
    user="root", 
    password="password", 
    database="pkmstunting",
    auth_plugin='mysql_native_password' )
cursor = db.cursor()

@app.route('/')
def regis():
    return render_template('login.html')

@app.route("/login", methods = ['POST', 'GET'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    query = 'SELECT * FROM user WHERE nama = %s AND password = %s'
    insert =  (username, password)

    cursor.execute(query,insert)
    user = cursor.fetchone()

    if username and password not in user:
        return redirect('/register')

    if user:
        session["user"] = username
        return redirect('/sukses')
    

@app.route('/register', methods=['GET','POST'])
def register():
    nama = request.form.get('nama')
    password = request.form.get('password')
    alamat = request.form.get('alamat')
    tanggalLahir = request.form.get('tanggalLahir')
    jenisKelamin = request.form.get('jenisKelamin')

    sql = 'INSERT INTO user(nama,password,alamat,tanggalLahir,jenisKelamin) VALUES(%s,%s,%s,%s,%s)'
    value =  (nama, password ,alamat ,tanggalLahir, jenisKelamin)

    cursor.execute(sql,value)
    db.commit()

    return render_template('home.html')


@app.route('/sukses')
def sukses():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
