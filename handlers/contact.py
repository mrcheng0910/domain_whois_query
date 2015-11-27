# encoding:utf-8
"""
查询域名whois信息
"""
import tornado.web

class ContactHandler(tornado.web.RequestHandler):
    """联系我们信息"""
    def get(self):
        self.render('contact.html')