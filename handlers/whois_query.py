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
        self.render(HTML_PATH+'whois_query.html',
                    domain="",
                    server="",
                    reg_org="",
                    reg_name="",
                    reg_phone="",
                    reg_email="",
                    creation_date="",
                    updated_date="",
                    expiration_date=""
                    )

    def post(self):
        domain = self.get_argument('domain', "None")
        whois = DomainWhoisDb().domain_whois(domain)
        print whois
        # self.write(json.dumps(domain_whois,cls=ComplexEncoder))
        self.render(HTML_PATH+'whois_query.html',
                    domain=domain,
                    server=whois[0]['top_whois_server'],
                    reg_org=whois[0]['org_name'],
                    reg_name=whois[0]['reg_name'],
                    reg_phone=whois[0]['reg_phone'],
                    reg_email=whois[0]['reg_email'],
                    creation_date=whois[0]['creation_date'],
                    updated_date=whois[0]['updated_date'],
                    expiration_date=whois[0]['expiration_date']
                    )


class ComplexEncoder(json.JSONEncoder):
    """json支持datetime格式数据"""
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        else:
            return json.JSONEncoder.default(self, obj)