# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 20:42:58 2018

@author: 89288
"""

from lxml import etree


class HtmlParser():
    
    def parser_url(self,response):
        '''
        解析网页
        return:返回文本的信息迭代器
        '''
        selector = etree.HTML(response)
        tags = selector.xpath('//tr[@class="item"]')
        
        for tag in tags:

            text_title = tag.xpath('td[2]/div[@class="pl2"]/a/@title')[0]
            
            book_information = tag.xpath('td[2]/p[@class="pl"]/text()')[0]
            list_information = book_information.split('/')
            
            author = list_information[0]
            publisher = list_information[-3]
            
            rating_nums = tag.xpath('td[2]/div[@class="star clearfix"]/\
                                    span[@class="rating_nums"]/text()')[0]
            dic_book = {'title':text_title,'author':author,
                        'publisher':publisher,'rating_nums':rating_nums}
            
            yield dic_book

