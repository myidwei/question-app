# -*- coding: UTF-8 -*-
from database import db
def column_dict(self):  
    model_dict = dict(self.__dict__)  
    del model_dict['_sa_instance_state']  
    return model_dict  
db.Model.column_dict = column_dict

class Questions(db.Model):
    __tablename__ = 'questions'
    id = db.Column(db.Integer, primary_key=True)
    question = db.Column(db.String(250), nullable=False, index=True)
    answer = db.Column(db.Text, nullable=False, index=False)
    category_id = db.Column(db.Integer,nullable=True,index=True)
    status = db.Column(db.String(20), primary_key=False,index=True)
    user_id = db.Column(db.Integer, primary_key=False,index=True)
    address = db.Column(db.String(250), nullable=False, index=True)
    longitude = db.Column(db.Float, nullable=False, index=True)
    latitude = db.Column(db.Float, nullable=False, index=True)
    created_at = db.Column(db.Integer,nullable=False,index=True)
    first_name = db.Column(db.String(40), nullable=False, index=False)
    last_name = db.Column(db.String(40), nullable=False, index=False)
    contact = db.Column(db.String(50), nullable=False, index=False)

    def __repr__(self):
        return '<Question %r>' % self.id

class RegUser(db.Model):
    __tablename__ = 'reg_user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False, index=True)
    password = db.Column(db.String(100), nullable=False, index=False)
    first_name = db.Column(db.String(100), nullable=False, index=False)
    last_name = db.Column(db.String(100), nullable=False, index=False)
    level = db.Column(db.String(50), nullable=False, index=False)
    status = db.Column(db.Integer, nullable=False, index=True)
    active_key = db.Column(db.String(100), nullable=False, index=False)
    reg_time = db.Column(db.Integer, nullable=False, index=True)
    def __repr__(self):
        return '<RegUser %r>' % self.id

class Tags(db.Model):
    __tablename__ = 'tags'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False, index=True)

class QuestionTagRel(db.Model):
    __tablename__ = 'question_tag_rel'
    tag_id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, primary_key=True)

class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(100), primary_key=False)