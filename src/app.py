from os import name
from flask import Flask
from flask import render_template
from flaskext.mysql import MySQL

app = Flask(__name__)
mysql = MySQL()

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3337
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'empleados'

mysql.init_app(app)

@app.route('/')
def index():
  sql = "insert into empleados (nombre, correo, foto) values ('Franco', 'mail@mail.com', 'fotoDeFranco.jpg');"

  con = mysql.connect()
  cur = con.cursor()
  cur.execute(sql)

  con.commit()

  return render_template('empleados/index.html')


if __name__ == '__main__':
  app.run(debug=True)

