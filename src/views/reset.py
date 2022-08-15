#导入前台请求的request模块
from flask import Blueprint, render_template, redirect,url_for
from flask import request 
from form import ResetForm
import re
import traceback

#传递根目录
reset = Blueprint('reset', __name__)



#更改密码格式
#强密码(以字母开头，必须包含大小写字母和数字的组合，不能使用特殊字符，长度在8-36之间)
#password_pattern = re.compile(r'[a-zA-Z](?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,36}')
password_pattern = re.compile(r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[\s\S]{8,36}')



#加入一些东西试试
@reset.route('/') 
def reset_modify():
    return render_template('reset.html',form=ResetForm())
    #获取注册请求及处理


@reset.route('/', methods=['POST'])
def mysqlmodify():
    from models import User, OnlineUser
    try:
        form = ResetForm()
        #assert form.validate_on_submit(), 'invalid form fields  不存在该用户！'
        username = form.username.data
        user = User.get_by(username=username)
        #assert username, 'invalid form fields  不存在该用户！'
        assert user, 'incorrect username or password   用户名或密码错误！不存在该用户！'

        password = form.password.data
        #password=reset_password
        assert password_pattern.fullmatch(password), 'invalid password   不合法的密码！'
        hash_password = form.get_hash_password()
        User.reset_user(username, hash_password)
        return redirect('/login')
    except AssertionError as e:
        message = e.args[0] if len(e.args) else str(e)
        return render_template('reset.html', form=ResetForm(), message=message)







# @reset.route('/mysqlmodify') 

# def mysqlmodify():
# #.打开数据库连接
# db=pymysql.connect("localhost","root","zhouxuyang1"，"denglu")

# #使用cursor()方法创建一个游标对象
# cursor cursor=db.cursor()
# sql = "select * from testdenglu where username=!" + request.args.get('username') + "'"
# #sql.=."update.testdenglu..set.password=!" +. request.args.get('password')+"! where. username=’".+. request.args. get( 'username')+"
# print(sql)
# modify_message='修改密码成功' 
# try:
#     #执行sql语句
#     cursor.execute(sql)
#     results=cursor.fetchall() 
#     print(len(results)) 
#     if len(results) == 1:
#         sql = "update testdenglu set password='" + request.args.get('password') + "'where username'" +request.args.get('username') + "'" 
#         cursor.execute(sql)
#         #提交到数据库执行 
#         db.commit()
#         return render_template('login.html',modify_message= modify_message) 
#     else:
#         return"用户名不存在"