import json
import os
import behave2cucumber
from behave import *

def after_all(context):
    with open('./report/report.json') as behave_json:
        cucumber_json = behave2cucumber.convert(json.load(behave_json))
        arquivo = open('.resultado-teste.json','w')                
        arquivo.write(str(cucumber_json).replace("'",'"'))
        arquivo.close()