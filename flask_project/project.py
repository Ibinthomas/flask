from flask import Flask, render_template,request
import sqlite3
app = Flask(__name__)


@app.route('/index')
def index1():
    return '<h1>Hello, world!</h1>'

@app.route('/ss',methods=['GET','POST'])
def index():
    if request.method == 'POST':
        name=request.form['name']
        age=request.form['age']
        print(name,age)

    return render_template('index.html')


@app.route('/',methods=['POST','GET'])
def fun2():
    if request.method=='POST':
        name=request.form['name']
        place=request.form['place']
        print(name,place)
        con=sqlite3.connect("user.db")
        try:
            con.execute("create table user (name text,place text)")
        except:
            pass
        con.execute("insert into user(name,place) values(?,?)",(name,place))
        con.commit()
    return render_template('index.html')

        
        
       



app.run()