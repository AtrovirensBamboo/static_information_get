# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 15:35:37 2018

@author: 89288
"""

import requests
import chardet

class HtmlDownloader():
    
        
    def download(self,url):
        '''
        下载链接对应的html内容
        return:返回字典{'response':response.text,'encoding':encoding_type}
        '''
        
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit\
        /537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core\
        /1.53.4549.400 QQBrowser/9.7.12900.400'
        
        refer = 'https://book.douban.com'
        headers = {'User-Agent':user_agent,'Refer':refer}
        
        try:
            response = requests.get(url,headers=headers)
            
            if response.status_code == 200:
                encoding_type = chardet.detect(response.content)['encoding']
                response.encoding = encoding_type
                
                return {'response':response.text,'encoding':encoding_type}
            else:
                return response.status_code
        except:
            return None
    
    
    

