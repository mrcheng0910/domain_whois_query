#coding=utf-8
"""
系统路由设置
"""
from handlers.index import IndexHandler
from handlers.whois_query import DomainWhoisHandler
from handlers.contact import ContactHandler
urls = [
    (r'/', IndexHandler),
    (r'/whois',DomainWhoisHandler),
    (r'/contact',ContactHandler),

]
