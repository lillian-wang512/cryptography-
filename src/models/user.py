from sqlalchemy import Column, String, Integer, Binary
from sqlalchemy import TIMESTAMP
from sqlalchemy.sql import func
from database import db
from flask import request
from flask_sqlalchemy import SQLAlchemy
#加入
# import hashlib
# import os


class User(db.Model):
    __tablename__ = 'users'

    id_ = Column(Integer, primary_key=True, autoincrement=True)
    create_time = Column(TIMESTAMP, default=func.now())
    username = Column(String(64), unique=True)
    hash_password = Column(Binary(64))
    encrypted_symmetric_key = Column(Binary(32), nullable=False)
    encrypted_private_key = Column(Binary(32), nullable=False)
    encrypted_public_key = Column(Binary(32), nullable=False)

    @classmethod
    def get_by(cls, **kwargs):
        return cls.query.filter_by(**kwargs).first()

    @classmethod
    def create_user(cls, username, hash_password):
        import secret
        user = User.get_by(username=username)
        #assert user is None, 'email already registered'
        assert user is None, '该用户已经被注册过了'


        # salt = os.urandom(16)
        # hash = hashlib.pbkdf2_hmac('sha256', b'password', salt, 100000)


        # 先随机生成一个用户的对称密钥与公私钥
        symmetric_key = secret.new_symmetric_key()
        private_key, public_key = secret.new_pair()
        # 再用服务器的公钥加密这些密钥
        user = User(username=username, hash_password=hash_password,
                    encrypted_symmetric_key=secret.encrypt(symmetric_key),
                    encrypted_private_key=secret.encrypt(private_key),
                    encrypted_public_key=secret.encrypt(public_key)
                    )
        db.session.add(user)
        db.session.commit()

    @classmethod
    def reset_user(cls, username, hash_password):
        import secret,requests
        #user = User.get_by(username=username)
        #assert user is None, 'email already registered'
        # id = request.args.get("username")
        # db = SQLAlchemy()
        # db.deletedata(id)
        # note=Note.query.get(username)
        # db.session.delete(note)
        #db.session.query(User).filter(User.username).delete()

        user=User.query.filter(User.username == username).first()
        user.hash_password=hash_password
        db.session.commit()




        # db.session.query(User).filter(User.username==username).delete()

        # #db.session.commit()


        # # 先随机生成一个用户的对称密钥与公私钥
        # symmetric_key = secret.new_symmetric_key()
        # private_key, public_key = secret.new_pair()
        # # 再用服务器的公钥加密这些密钥
        # user = User(username=username, hash_password=hash_password,
        #             encrypted_symmetric_key=secret.encrypt(symmetric_key),
        #             encrypted_private_key=secret.encrypt(private_key),
        #             encrypted_public_key=secret.encrypt(public_key)
        #             )
        # db.session.add(user)
        # db.session.commit()