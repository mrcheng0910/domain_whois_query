# encoding:utf-8
"""
查询域名whois信息
"""
import tornado.web

HTML_PATH = "./query_whois/"


class DomainWhoisHandler(tornado.web.RequestHandler):
    """查询域名whois信息"""
    def get(self):
        self.render(HTML_PATH+'whois_query.html',
                    title="域名whois查询")
