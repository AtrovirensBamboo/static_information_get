# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

class UrlManager():
    
    def __init__(self):
        '''
        get_urls:需要爬取的链接
        reload_urls:爬取失败的链接
        got_urls:已爬取链接
        '''
        pre_url = r'https://book.douban.com/top250?start='
        list_numbers = list(range(0,226,25))
        
        urls = []
        for list_number in list_numbers:
            url = pre_url + str(list_number)
            urls.append(url)
        self.get_urls = urls[:]
        self.reload_urls = []
        self.got_urls = []
        
    def get_url(self):
        '''
        从需要爬取的链接中取出一个链接
        return:返回链接
        '''
        url = self.get_urls.pop(0)
        return url

        
    def add_got_url(self,url):
        '''
        将已爬取的链接加入已爬取链接列表
        '''
        self.got_urls.append(url)
        
    def add_reload_url(self,url):
        '''
        将爬取失败的链接加入列表
        '''
        
        self.reload_urls.append(url)

