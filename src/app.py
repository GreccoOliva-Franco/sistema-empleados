import os
from dotenv import load_dotenv
from flask import Flask
from flask import render_template, request
from flaskext.mysql import MySQL
from werkzeug.utils import redirect

# Settings
load_dotenv('../.env')
app = Flask(__name__)
app.config['MYSQL_DATABASE_HOST'] = os.environ('MYSQL_DATABASE_HOST')
app.config['MYSQL_DATABASE_PORT'] = os.environ('MYSQL_DATABASE_PORT')
app.config['MYSQL_DATABASE_USER'] = os.environ('MYSQL_DATABASE_USER')
app.config['MYSQL_DATABASE_PASSWORD'] = os.environ('MYSQL_DATABASE_PASSWORD')
app.config['MYSQL_DATABASE_DB'] = os.environ('MYSQL_DATABASE_DB')

mysql = MySQL()
mysql.init_app(app)


# Routes
@app.route('/')
def home():
  sql = "SELECT * FROM empleados"
  empleados = mysql.connect().cursor().execute(sql).commit()
  
  return render_template('empleados/index.html', empleados=empleados)

@app.route('/register')
def createEmployee():
  return render_template("empleados/register.html")

@app.route("/register-save", methods=['POST'])
def storeEmployee():
  _name = request.form["userName"]
  _mail = request.form["userMail"]
  _photo = request.files['userPhoto']

  sql = "INSERT INTO empleados (name, mail, photoPath) VALUES (%s, %s, %s)"
  values = (_name, _mail, _photo)

  con = mysql.connect()
  cur = con.cursor()
  cur.execute(sql, values)
  con.commit()
  
  return redirect('empleados/index.html')

@app.route('/edit', methods=['PUT'])
def modifyEmployee():
  pass

@app.route('/delete')
def deleteEmployee():
  pass
  


if __name__ == '__main__':
  app.run(debug=True)