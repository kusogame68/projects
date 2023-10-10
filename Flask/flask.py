# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 22:14:45 2023

@author: User
"""


from flask import Flask
from flask import redirect,url_for
from flask import render_template
from flask import request

app=Flask(__name__)
 
#route
#顯示/
@app.route('/hello/')
@app.route('/hello/<path:name>')
def hello1(name=None):
    if name == None:
        return 'name is None'
    return f'hello {name}!!!!'

@app.route('/johnson')
def johnson():
    return 'hello johnson'

#<>
#導入另一個def
@app.route('/456/')
@app.route('/456/<name1>')
def hello2(name1=None):
    if name1==None:
        return redirect(url_for('johnson'))
    return redirect(url_for('hello1',name=name1))

#導入html檔
@app.route('/123/<user>')
def h_t_m_l(user):
    return render_template('hello.html',name=user)

#透過html直接導入route
@app.route('/login',methods=['POST','GET'])
def get_name():
    if request.method == 'POST':
        user=request.form['name'] #form:表單
        return redirect(url_for('hello2',name1=user))
    else:
        user=request.args.get('name')
        print(request.args)
        return redirect(url_for('h_t_m_l',user=user))    

@app.route('/admin')    
def h_admin():
    return 'Hello admin123456'

@app.route('/user/')
@app.route('/user/<user>')
def g_admin(user=None):
    if user==None:
        return redirect(url_for('h_admin'))
    return render_template('test1.html',name=user)
    

if __name__ == '__main__':
    app.run(debug='True',host='127.0.0.1',port='8000')