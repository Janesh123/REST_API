from flask import Flask
from flask import request
from flask_mysqldb import MySQL
from flask import redirect
from flask import url_for
from flask import render_template

app=Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='9820587794'
app.config['MYSQL_DB']='movie_ticket'

mysql=MySQL(app)

@app.route('/')
def welcome():
	return render_template('home.html')

@app.route('/book')
def showmovies():
	cur=mysql.connection.cursor()
	cur.execute("SELECT * FROM movies")
	fetchdata=cur.fetchall()
	print(list(fetchdata))
	cur.close()
	return render_template('book.html',data=fetchdata)
	
@app.route('/checkout', methods=['POST','GET'])
def checkout():
	if request.method=="POST":
		x=request.form['mov']
		cur=mysql.connection.cursor()
		cur.execute("SELECT * FROM movies WHERE id =%s",(x))
		fetchdata=cur.fetchall()
		print(fetchdata)
		cur.close()
		return render_template('checkout.html')
	
	

if __name__ == '__main__':
	app.run(debug=True)
