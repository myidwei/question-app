# -*- coding: UTF-8 -*-
from flask import Flask
import time, datetime
from models import *
from database import *
from flask import jsonify, request, make_response, session
import json
import os
from gevent.pywsgi import WSGIServer
from users import users
from manage import manage
from commons import *


app = create_app()
app.config['SECRET_KEY'] = os.urandom(24)
app.register_blueprint(users, url_prefix='/users')
app.register_blueprint(manage, url_prefix='/manage')

#website homepage
@app.route('/')
def search_page():
    return app.send_static_file('homepage.html')

#add new question
@app.route('/add')
def add_page():
    return app.send_static_file('add.html')

#list all questions
@app.route('/question/all')
def get_all():
    all = db.session.query(Questions).all() 
    return success(all)

#submit new question
@app.route('/question/submit',methods=["POST"])
def add():
    data = json.loads(request.get_data(as_text=True))
    question = data['question']
    first_name = data['first_name']
    last_name = data['last_name']
    category_id = data['category_id']
    tags = data['tags']
    contact = data['contact']
    
    created_at = int(time.time())
    obj = Questions(question=question,answer='',status='submitted',first_name=first_name,last_name=last_name,contact=contact,category_id=category_id,created_at=created_at)
    db.session.add(obj)
    db.session.commit()
    for tag_id in tags:
        tag_rel = QuestionTagRel(tag_id=tag_id,question_id=obj.id)
        db.session.add(tag_rel)
    db.session.commit()
    return success(obj.id)


#sugguest
@app.route('/question/sugguest/<keyword>',methods=["GET"])
def sugguest(keyword):
    result = []
    if keyword == '':
        return result
    #tags
    query = db.session.query(Tags).filter(Tags.name.like('%'+keyword+'%'))
    rows = query.limit(3).all()
    for row in rows:
        result.append({'type':'Tag','value':row.name,'id':row.id})
    #questions
    query = db.session.query(Questions).filter(Questions.question.like('%'+keyword+'%')).filter(Questions.status == 'published')
    count = query.count()
    rows = query.order_by(Questions.created_at.desc()).limit(3).all()
    for row in rows:
        result.append({'type':'Question','value':row.question,'id':row.id})
    return success({'list':result})

@app.route('/question/search',methods=["POST"])
def search():
    data = json.loads(request.get_data(as_text=True))
    keyword = ''
    page = 1
    size = 20
    if data.has_key('keyword'):
        keyword = data['keyword']
    if data.has_key('page'):
        page = int(data['page'])
    if data.has_key('size'):
        size = int(data['size'])
    result = []

    if keyword.startswith('tag:'):
        tag_str = keyword[4:]
        tag = get_tag_by_name(tag_str)
        if tag == None:
            return failed(-1,'Tag not found')
        return get_by_tag(str(tag.id),str(page))
    else:
        query = db.session.query(Questions).filter(Questions.question.like('%'+keyword+'%')).filter(Questions.status == 'published')
        count = query.count()
        rows = query.order_by(Questions.created_at.desc()).limit(size).offset((page-1)*size).all()
        for row in rows:
            item = row.column_dict()
            tags = get_tags(row.id)
            item['tags'] = tags
            result.append(item)
    return success({'total':count,'list':result})

#question by tag
@app.route('/question/tag/<id>/<page>',methods=["GET"])
def get_by_tag(id,page):
    size = 20
    result = []
    sql = "select a.id,a.question,a.answer,a.category_id,a.status,a.user_id,a.longitude,a.latitude,a.created_at from questions a inner join question_tag_rel b on a.id=b.question_id where b.tag_id=" + id + " and a.status='published' order by created_at desc limit " + str((int(page) - 1) * size) + "," + str(size)
    countSql = "select count(*) from questions a inner join question_tag_rel b on a.id=b.question_id where b.tag_id=" + id + " and a.status='published'";
    rows = db.session.execute(sql).fetchall()
    count = db.session.execute(countSql).fetchone()
    if count == None :
        count = (0,)
    data = []
    for item in rows:
        obj = {'id':item[0],'question':item[1],'answer':item[2],'category_id':item[3],'status':item[4],'user_id':item[5],'longitude':item[6],'latitude':item[7],'created_at':item[8]}
        obj['tags'] = get_tags(obj['id'])

        data.append(obj)
    return success({'total':count[0],'list':data})

if __name__ == '__main__':
    app.run(host='0.0.0.0')
    http_serve = WSGIServer(("0.0.0.0",5000),app)
    http_serve.serve_forever()
