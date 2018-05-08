# coding='utf-8'

from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from flask import url_for


# db实例化对象不再传入　app对象
# 创建数据库ORM对象
db = SQLAlchemy()

# 创建基类，方便以后创建的表使用
class Base(db.Model, UserMixin):
    # 继承UserMixin 使用is_authenticated property() 判断用户是否登录状态

    """ 所有model的一个基类，默认添加了时间戳"""
    # 不要把这个表当做 Model类, 即不在数据库中创建该表,可以当做基类
    __abstract__ = True
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

