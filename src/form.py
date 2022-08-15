from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, FileField
from wtforms.validators import DataRequired
import hashlib


class PasswordForm(FlaskForm):
    password = PasswordField('password', validators=[DataRequired()])

    def get_hash_password(self):
        from hashlib import sha512
        #return sha512(self.password.data.encode()).digest()
        
        hash = sha512(self.password.data.encode())
        hash.update('admin'.encode('utf-8'))
        return hash.digest()


        # from hashlib import sha512
        # import os
        # salt = os.urandom(16)
        # hash_word = hashlib.pbkdf2_hmac('sha512', self.password, salt, 100000)
        # #return sha512(self.password.data.encode()).digest()
        # return salt,hash_word


class RegisterForm(PasswordForm):
    username = StringField('username', validators=[DataRequired()])
    confirm_password = PasswordField('confirm_password', validators=[DataRequired()])


class LoginForm(PasswordForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])


class FileForm(FlaskForm):
    from flask_wtf.file import FileRequired
    file = FileField('file', validators=[FileRequired()])

class ResetForm(PasswordForm):
    username = StringField('username', validators=[DataRequired()])
    password = PasswordField('password', validators=[DataRequired()])

    # def get_hash_password(self):
    #     # from hashlib import sha512
    #     # # import os
    #     # # salt = os.urandom(16)
    #     # # hash_word = hashlib.pbkdf2_hmac('sha512', password, salt, 100000)
    #     # return sha512(self.password.data.encode()).digest()
    #     # # return salt,hash_word

    #     from hashlib import sha512
    #     #return sha512(self.password.data.encode()).digest()
        
    #     hash = sha512(self.password.data.encode())
    #     hash.update('admin'.encode('utf-8'))
    #     return hash.digest
