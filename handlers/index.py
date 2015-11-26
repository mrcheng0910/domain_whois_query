# encoding:utf-8
"""
首页handler
"""
import tornado.web


class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')
