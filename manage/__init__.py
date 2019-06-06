from flask import Blueprint
import os
manage = Blueprint("Manage",__name__,static_folder='static')
from manage import views