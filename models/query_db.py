# encoding:utf-8
"""
查询某域名的whois信息
"""
import json
from base_db import BaseDb

class DomainWhoisDb(BaseDb):

    def __init__(self):
        BaseDb.__init__(self)  # 执行父类

    def domain_whois(self,domain=""):
        """获取域名的whois信息"""
        domain_initial = self.extract_initial(domain)
        sql = " SELECT domain,top_whois_server,reg_email,reg_name,\
                reg_phone,org_name,creation_date,expiration_date,updated_date,\
                domain_details,insert_time FROM domain_whois_%s WHERE domain='%s'" % (domain_initial,domain)
        domains = self.db.query(sql)
        return domains

    def extract_initial(self,domain=""):
        """提取域名的首字母，用来选取表,主要是针对特殊字母进行处理"""
        initial = domain[0]
        return initial.upper()


