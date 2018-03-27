from flask import Flask
from flask import request
from flask import render_template
from flask import redirect,url_for
from datetime import datetime
import pymongo

from database import Database

app=Flask(__name__)
app.secret_key = 'some_secret'

@app.before_first_request
def initialize_database():
    Database.initialize()

@app.route('/show')
def show_entries():
    entries=Database.get_records()
    return render_template('base_entry.html',entries=entries)

@app.route('/add', methods=['GET','POST'] )
def add_entry():
    print('hello')
    if request.method=="POST":
        print('hello')
        name=request.form.get('name')
        school=request.form.get('school')
        classes=request.form.get('classes')
        address= request.form.get('address')
        email= request.form.get('email')
        phone_number= request.form.get('phone_number')
        city=request.form.get('city')
        text=request.form.get('text')

        doc={
            'name':name,
            'school':school,
            'classes':classes,
            'address': address,
            'email': email,
            'phone_number': phone_number,
            'city':city,
            'text':text,
            'date_time':datetime.now().strftime("Date: %A %Y %m %d Time:%I:%M:%S %r")
        }
        print ('insert data')
        Database.insert_record(doc)
        return redirect('show')
    return render_template('add_entries.html')

@app.route('/remove', methods=['GET','POST'] )
def remove_entry():
    if request.method=="POST":
        name=request.form.get('name')
        doc={'name':name}
        Database.delete_one(doc)

        return redirect('show')
    return render_template('remove_entry.html')

@app.route('/update', methods=['GET','POST'])
def update_entry():
    if request.method=='POST':
        find_name=request.form.get('find_name')
        name=request.form.get('name')
        school=request.form.get('school')
        classes=request.form.get('class')
        address=request.form.get('address')
        email = request.form.get('email')
        phone_number = request.form.get('phone_number')
        city = request.form.get('city')
        text=request.form.get('text')
        arg={'name':find_name}
        doc = {
            'name': name,
            'school':school,
            'classes':classes,
            'address': address,
            'email': email,
            'phone_number': phone_number,
            'city': city,
            'text':text,
            'date_time':datetime.now()
        }
        Database.update_one(arg,doc)
        #flash('You were successfully logged in')
        return redirect('show')
    return render_template('update_entry.html')

@app.route('/edit/<string:id>', methods=['GET','POST'])
def edit_entry(id):
    print(id)
    if request.method=='POST':

        #find_name=request.form.get('id')
        #print('find=',find_name)
        name=request.form.get('name')
        school=request.form.get('school')
        classes=request.form.get('class')
        address=request.form.get('address')
        email = request.form.get('email')
        phone_number = request.form.get('phone_number')
        city = request.form.get('city')
        text=request.form.get('text')
        arg={'name':id}
        doc = {
            'name': name,
            'school':school,
            'classes':classes,
            'address': address,
            'email': email,
            'phone_number': phone_number,
            'city': city,
            'text':text,
            'date_time':datetime.now()
        }
        Database.update_one(arg,doc)
        #flash('You were successfully logged in')
        return redirect('show')
    return render_template('edit_entry.html',id=id)

@app.route('/delete')
def delete_all():
    Database.delete_all()
    return redirect(url_for('show_entries'))

@app.route('/')
def home():
    users = [
        {'name': 'Anne','age':13,'city':'San Jose','state':'CA'},
        {'name': 'Bob','age':23,'city':'Fremont','state':'CA'},
        {'name': 'Steve','age':11, 'city':'Sunnyvale','state':'CA'},
        {'name': 'Richard','age':21,'city':'Union City','state':'CA'},
        {'name': 'Mike','age':19,'city':'Milpitas','state':'CA'},

    ]

    user = request.args.get('user')
    age = request.args.get('age')
    city = request.args.get('city')
    state = request.args.get('state')
    users.append({'name':user,'age':age,'city':city,'state':state})



    #user = request.args.get('user')
    return render_template ('menu.html',name=users)


@app.route('/login',methods=['GET','POST'])
def login():

    print ('hello world')
    if request.method=='GET':
        return render_template('login.html')
    if request.method=='POST':
        user = request.form.get('user')
        age = request.form.get('age')
        city = request.form.get('city')
        state = request.form.get('state')
        print('redirecting...',user)
        return redirect(url_for('home',user=user,age=age,city=city,state=state))




if __name__=='__main__':
    app.run(debug=True)
