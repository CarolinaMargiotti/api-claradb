import os
from flask import Blueprint

from src.models.example import helloWorld as hello
from src.models.example import homeFunction as home

routes_bp = Blueprint("routes",__name__)

@routes_bp.route("/",methods=['GET'])
def homeRoute():
    return home()

@routes_bp.route("/hello",methods=['GET'])
def helloWorld():
    return hello();

