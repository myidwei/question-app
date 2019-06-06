from manage import manage
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
import json
from models import *
from database import *
import random
import string
import time, datetime
from commons import *


#check if user login
def is_login():
    user = session.get('login_user')
    return user != None

#manage index page
@manage.route('/index')
def index_page():
    if is_login():
        return manage.send_static_file('index.html')
    else:
        return redirect(url_for('Users.login_page'))

#get one question
@manage.route('/question/<id>',methods=["GET"])
def find(id):
    row = db.session.query(Questions).filter_by(id=id).first()
    if row == None:
        return failed(-1,'Data not found')
    ret = row.column_dict()
    tags = get_tags_info(row.id)
    ret['tags'] = tags
    return success(ret)

#add or update question page
@manage.route('/question/update_question')
def update_question():
    return manage.send_static_file('update_question.html')

#do update question
@manage.route('/question/update',methods=["POST"])
def update():
    user = user_info()
    if user == None:
        return failed(403,'Need Login')
    data = json.loads(request.get_data(as_text=True))
    if data['id'] != "0":
        row = db.session.query(Questions).filter_by(id=data['id']).first()
        if row == None:
            return failed(-1,'Data not found')
        row.question = data['question']
        row.answer =data['answer']
        row.first_name = data['first_name']
        row.last_name = data['last_name']
        row.contact = data['contact']
        row.category_id = data['category_id']
        row.status = data['status']
        row.user_id = user.id
        db.session.commit()
    else:
        question = data['question']
        first_name = data['first_name']
        last_name = data['last_name']
        category_id = data['category_id']
        tags = data['tags']
        contact = data['contact']
        answer = data['answer']
        status = data['status']
        created_at = int(time.time())
        row = Questions(user_id=user.id,question=question,answer=answer,status=status,first_name=first_name,last_name=last_name,contact=contact,category_id=category_id,created_at=created_at)
        db.session.add(row)
        db.session.commit()
    
    tag_items = db.session.query(QuestionTagRel).filter(QuestionTagRel.question_id==row.id).all()
    for item in tag_items:
        db.session.delete(item)
    db.session.commit()
    tags = data['tags']
    for tag_id in tags:
        tag_rel = QuestionTagRel(tag_id=tag_id,question_id=row.id)
        db.session.add(tag_rel)
    db.session.commit()
    return success(row.id)

#manage search
@manage.route('/question/manage_search',methods=["POST"])
def manage_search():
    user = user_info()
    if user == None:
        return failed(403,'Need Login')
    data = json.loads(request.get_data(as_text=True))
    keyword = ''
    page = 1
    size = 20
    status = ''
    if data.has_key('keyword'):
        keyword = data['keyword']
    if data.has_key('page'):
        page = int(data['page'])
    if data.has_key('size'):
        size = int(data['size'])
    if data.has_key('status'):
        status = data['status']
    result = []
    filters = {Questions.status == status} 
    if user.level == 'staff' and status == 'pending':
        filters.add(Questions.user_id == user.id)
    query = db.session.query(Questions).filter(Questions.question.like('%'+keyword+'%')).filter(*filters)

    count = query.count()
    rows = query.order_by(Questions.created_at.desc()).limit(size).offset((page-1)*size).all()
    for row in rows:
        item = row.column_dict()
        tags = get_tags(row.id)
        item['tags'] = tags
        result.append(item)
        
    return success({'total':count,'list':result})

#delete question
@manage.route('/question/del',methods=["POST"])
def delete():
    user = user_info()
    if user == None:
        return failed(403,'Need Login')
    data = json.loads(request.get_data(as_text=True))
    row = db.session.query(Questions).filter_by(id=data['id']).first()
    if row == None:
        return failed(-1,'Data not found')
    db.session.delete(row)
    db.session.commit()
    return success(0)

#load all category
@manage.route('/category/all',methods=["GET"])
def all_category():
    return success(convert_dict(get_category_list()))

#load all tags
@manage.route('/tags/all',methods=["GET"])
def all_tags():
    return success(convert_dict(get_tag_list()))

#load base data 
@manage.route('/data/base_data',methods=["GET"])
def all_tag_and_category():
    return success({'tags':convert_dict(get_tag_list()),'categories':convert_dict(get_category_list())})
