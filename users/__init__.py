from flask import Blueprint
import os
users = Blueprint("Users",__name__,static_folder='static')
from users import views