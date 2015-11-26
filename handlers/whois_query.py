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
        if not whois:
            # self.write("wu")
            self.redirect('/whois')
        # self.write(json.dumps(domain_whois,cls=ComplexEncoder))
        self.render(HTML_PATH+'whois_query.html',
                    domain=domain,
                    server=whois[0].get('top_whois_server',None),
                    reg_org=whois[0].get('org_name',None),
                    reg_name=whois[0].get('reg_name',None),
                    reg_phone=whois[0].get('reg_phone',None),
                    reg_email=whois[0].get('reg_email',None),
                    creation_date=whois[0].get('creation_date',None),
                    updated_date=whois[0].get('updated_date',None),
                    expiration_date=whois[0].get('expiration_date',None)
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