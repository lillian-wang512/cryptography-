from flask import Blueprint, render_template, redirect
import re
#从form.py导入RegisterForm()
from form import RegisterForm

#引用蓝图分装函数
#创建蓝图
register = Blueprint('register', __name__)

#更改用户名
#中文、英文、数字但不包括下划线等符号，2-36位
username_pattern = re.compile(r'[\u4E00-\u9FA5A-Za-z0-9]{2,36}$')
# username_pattern = re.compile(r'[\u4e00-\u9fa5a-zA-Z0-9]+')

#更改密码格式
#强密码(以字母开头，必须包含大小写字母和数字的组合，不能使用特殊字符，长度在8-36之间)
#password_pattern = re.compile(r'[a-zA-Z](?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,36}')
password_pattern = re.compile(r'(?=.*[a-z])(?=.*[A-Z])(?=.*\d)[\s\S]{8,36}')


@register.route('/')
def get__register():
    return render_template('register.html', form=RegisterForm())


@register.route('/', methods=['POST'])
def post__register():
    #引入models.user模块
    from models import User

    try:
        form = RegisterForm()
        #把这行注释掉了，不然只会报错用户名或密码错误不会报别的错
        #assert form.validate_on_submit(), 'invalid form fields  用户名或密码错误！'
        username = form.username.data
        assert username_pattern.fullmatch(username), 'invalid username   不合法的用户名！'
        password = form.password.data
        confirm_password = form.confirm_password.data
        #更改顺序(后来发现不改也行)
        assert password_pattern.fullmatch(password), 'invalid password   不合法的密码！'
        # password = form.password.data
        # confirm_password = form.confirm_password.data
        assert password != confirm_password, 'mismatched password and confirm_password  两次输入密码不一致！'
        #assert password_pattern.fullmatch(password), 'invalid password   不合法的密码！'
        hash_password = form.get_hash_password()
        User.create_user(username, hash_password)
        return redirect('/login')
    except AssertionError as e:
        message = e.args[0] if len(e.args) else str(e)
        return render_template('register.html', form=RegisterForm(), message=message)
