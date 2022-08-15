#加了url_for,为了引入css
from flask import Blueprint, render_template, redirect,url_for
from form import LoginForm
from common import *

login = Blueprint('login', __name__)


@login.route('/')
def get__login():
    return render_template('login.html', form=LoginForm())


@login.route('/', methods=['POST'])
def post__login():
    from models import User, OnlineUser
    try:
        form = LoginForm()
        assert form.validate_on_submit(), 'invalid form fields  不存在该用户！'
        hash_password = form.get_hash_password()
        username = form.username.data
        user = User.get_by(username=username, hash_password=hash_password)
        #assert username, 'invalid form fields  不存在该用户！'
        assert user, 'incorrect username or password   用户名或密码错误！'
        token = OnlineUser.create_record(user.id_)
        return set_token(redirect('/'), token)
    except AssertionError as e:
        message = e.args[0] if len(e.args) else str(e)
        return render_template('login.html', form=LoginForm(), message=message)





# #加入一些东西试试
# @login.route('/reset') 
#     def reset_modify():
#         return render_template('reset.html')
#         #获取注册请求及处理


# @login.route('/reset', methods=['POST']') 
#     def mysqlmodify():
#         from models import User, OnlineUser
#     try:
#         form = ResetForm()
#         assert form.validate_on_submit(), 'invalid form fields  不存在该用户！'
#         password = form.password.data
#         assert password_pattern.fullmatch(password), 'invalid password   不合法的密码！'
#         hash_password = form.get_hash_password()
#         User.create_user(username, hash_password)
#         return redirect('/login')
#     except AssertionError as e:
#         message = e.args[0] if len(e.args) else str(e)
#         return render_template('register.html', form=RegisterForm(), message=message)


    #     hash_password = form.get_hash_password()
    #     username = form.username.data
    #     user = User.get_by(username=username, hash_password=hash_password)
    #     #assert username, 'invalid form fields  不存在该用户！'
    #     assert user, 'incorrect username or password   用户名或密码错误！'
    #     token = OnlineUser.create_record(user.id_)
    #     return set_token(redirect('/'), token)
    # except AssertionError as e:
    #     message = e.args[0] if len(e.args) else str(e)
    #     return render_template('login.html', form=LoginForm(), message=message)

# def mysqlmodify():
# #.打开数据库连接
#     db=pymysql.connect("localhost","root","zhouxuyang1","denglu")

#     #使用cursor()方法创建一个游标对象
#     cursor cursor=db.cursor()
#     sql = "select * from testdenglu where username=!" + request.args.get('username') + "'"
#     #sql.=."update.testdenglu..set.password=!" +. request.args.get('password')+"! where. username=’".+. request.args. get( 'username')+"
#     print(sql)
#     modify_message='修改密码成功' 
#     try:
#         #执行sql语句
#         cursor.execute(sql)
#         results=cursor.fetchall() 
#         print(len(results)) 
#         if len(results) == 1:
#             sql = "update testdenglu set password='" + request.args.get('password') + "'where username'" +request.args.get('username') + "'" 
#             cursor.execute(sql)
#             #提交到数据库执行 
#             db.commit()
#             return render_template('login.html',modify_message= modify_message) 
#         else:
#             return"用户名不存在"
