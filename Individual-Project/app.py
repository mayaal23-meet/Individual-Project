from flask import Flask, render_template, request, redirect, url_for, flash
from flask import session as login_session
import pyrebase

app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

#Code goes below here


app = Flask(__name__, template_folder='templates', static_folder='static')
app.config['SECRET_KEY'] = 'super-secret-key'

config = {
    "apiKey": "AIzaSyAZOng19U1Wj68AnWB5npXWQNO0QNo-ZyE",
    "authDomain": "cs-personal-proj.firebaseapp.com",
    "databaseURL": "https://cs-personal-proj-default-rtdb.europe-west1.firebasedatabase.app",
    "projectId": "cs-personal-proj",
    "storageBucket": "cs-personal-proj.appspot.com",
    "messagingSenderId": "343072918903",
    "appId": "1:343072918903:web:10888737522c5b46672572",
    "measurementId": "G-B959B144CM",
	"databaseURL":"https://cs-personal-proj-default-rtdb.europe-west1.firebasedatabase.app/"
}



firebase = pyrebase.initialize_app(config)
auth = firebase.auth()
db=firebase.database()

@app.route('/', methods=['GET', 'POST'])
def signup():
  error = ""
  if request.method == 'POST':
      name = request.form['name']
      email = request.form['email']
      password = request.form['password']

      try:
        login_session['user'] = auth.create_user_with_email_and_password(email, password)

        user= {'name':name,'email':email,'password':password}
        db.child('Users').child(login_session['user']['localId']).set(user)
        return redirect(url_for('signin'))
      except:
        error = "Authentication failed"
  else:
    return render_template('signup.html')



@app.route('/signin', methods=['GET', 'POST'])
def signin():
	error = ""
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']
		try:
			login_session['user'] = auth.sign_in_with_email_and_password(email, password)
			return redirect(url_for('home'))
		except:
			error = "Authentication failed"
	else:
		return render_template('signin.html')


@app.route('/home', methods=['GET','POST'])
def home():
	error=''
	if request.method=='POST':
		try:
			return render_tempate('home.html')
		except:
			error='Authentication failed'
	else:
		return render_template('index.html')


@app.route('/share', methods=['GET','POST'])
def share():
	if request.method=='POST':
		try:
			title = request.form['title']
			comment = request.form['comment']
			uid = login_session['user']['localId']
			comments = {"title":title,"comment":comment, "uid":uid}
			db.child('comments').push(comments)
			return redirect(url_for('home'))

		except:
			raise
			error = "couldn't post comment"
	else:
		return render_template("share.html")

@app.route('/upload',methods=['GET','POST'])
def upload():
	if request.method=='POST':
		try:
			name = request.form['name']
			explanation = request.form['explanation']
			uid = login_session['user']['localId']
			explanations = {"name":name,"explanation":explanation, "uid":uid}
			db.child('explanations').push(explanations)
			return redirect(url_for('home'))
		except:
			raise
			error = "couldn't post your project"

	else:
		return render_template("upload.html")


@app.route('/comments', methods=['GET','POST'])
def comments():
	if request.method=='POST':
		try:
			redirect(url_for('share'))
		except:
			error = "coldn't open comments"
	else:
		comments=db.child('comments').get().val()
		return render_template('all_comments.html',comments=comments)
	


#Code goes above here

if __name__ == '__main__':
    app.run(debug=True)