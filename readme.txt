一、安装说明
1、安装环境ubuntu18
    更新：
    apt update
    安装pip,mysql-client：
    apt install python-pip libmysqlclient-dev
    安装模块
    pip install flask poster flask_sqlalchemy mysql-python flask-socketio gevent-websocket
2、安装数据库，修改配置
    安装mysql
    apt install mysql-server
    设置root密码：
    mysqladmin -u root password 123456
    创建数据库question，并导入sql文件：question-database.sql
    修改配置文件：
    database.py
    将 app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://user:pass@server/database'
    修改为
    app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root:123456@localhost/question'
3、启动程序
   nohup python app.py &
4、访问：
    访问地址：
    http://server-ip:5000/
    后台地址：
    http://server-ip:5000/users/login
    admin用户：
    wattsappbronx@outlook.com
    密码1
二、程序说明
python框架：Flask
页面框架：Layui
question-database.sql：导入初始数据文件
database.py：数据库配置
commons.py：通用方法
app.py：程序入口
models.py：数据库实体类
static目录：前台的静态文件
manage目录：后台管理问题的模块
users目录：后台与用户相关的模块
