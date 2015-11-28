# encoding:utf-8
"""
查询域名whois信息
"""
import tornado.web
import json
from models.query_db import DomainWhoisDb # 域名查询数据库
from datetime import datetime,date

HTML_PATH = "./query_whois/"


class DomainWhoisHandler(tornado.web.RequestHandler):
    """查询域名whois信息"""
    def get(self):
        self.render(HTML_PATH+'query.html',)


class ComplexEncoder(json.JSONEncoder):
    """json支持datetime格式数据"""
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)

class WhoisQuery(tornado.web.RequestHandler):
    def get(self):
        domain = self.get_argument('domain', "None")
        domain_whois = DomainWhoisDb().domain_whois(domain)
        self.write(json.dumps(domain_whois,cls=ComplexEncoder))
