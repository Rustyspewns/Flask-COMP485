import sqlite3, smtplib, os, subprocess
from flask 
import Flask, request, session, g, render_template, flash
from contextlib 
import closing
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)
app.config.from_pyfile('config.cfg') # Initialize app's settings from config.cfg


def connect_db():
	return sqlite3.connect(app.config['DATABASE'])


def init_db():
	with app.app_context():
		db = get_db()
		with app.open_resource('schema.sql', mode='r') as f:
			db.cursor().executescript(f.read())
		db.commit()


@app.route('/addUser', methods=['GET', 'POST'])
def add_user():
	if not session.get('logged_in'):
		abort(401)


if __name__ == "__main__":
	app.run()
