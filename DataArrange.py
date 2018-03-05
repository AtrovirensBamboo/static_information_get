# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 15:51:49 2018

@author: 89288
"""

import pymongo

class DataArrange():
    
    def __init__(self):
        '''
        链接mongoDB
        '''
        client = pymongo.MongoClient('localhost',27017)
        self.db = client.douban
    
    def save_urls(self,dic_urls):
        '''
        将需要爬取的链接存入数据库
        return:返回mongodb定义的id值
        '''
        collection_urls = self.db.urls
        urls_id = collection_urls.insert(dic_urls)
        return urls_id
    
    def save_contents(self,dic_contents):
        '''
        将爬取的信息存入数据库集合
        return:返回mongodb的id值
        '''
        collection_contents = self.db.contents
        contents_id = collection_contents.insert(dic_contents)
        return contents_id
    
    def save_reload_urls(self,dic_url):
        '''
        将爬取失败的链接存入数据库
        return:返回mongodb的id值
        '''
        collection_reload_urls = self.db.reload_urls
        reload_url_id = collection_reload_urls.insert(dic_url)
        return reload_url_id
    
    def save_get_urls(self,dic_get_urls):
        '''
        将已爬取的链接存入数据库
        return:返回mongodb的id值
        '''
        collection_get_urls = self.db.get_urls
        get_urls_id = collection_get_urls.insert(dic_get_urls)
        return get_urls_id
    
    
    
    
    
    

