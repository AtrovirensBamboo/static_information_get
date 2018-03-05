# -*- coding: utf-8 -*-
"""
Created on Mon Mar  5 09:31:37 2018

@author: 89288
"""

import UrlManager as UM
import HtmlDownloader as HD
import HtmlParser as HP
import DataArrange as DA
import time


class WebCrawler():
    
    def __init__(self):
        
        self.UM = UM.UrlManager()
        self.HD = HD.HtmlDownloader()
        self.HP = HP.HtmlParser()
        self.DA = DA.DataArrange()
       
    def main_program(self):
        
        self.DA.save_urls({'urls':self.UM.get_urls})
        for url in self.UM.get_urls:
            html_download = self.HD.download(url)
            
            if type(html_download) is not dict:
                self.UM.add_reload_url(url)
            else:
                book_infors = self.HP.parser_url(html_download['response'])
                
                for book_info in book_infors:
                    self.DA.save_contents(book_info)
                
                self.UM.add_got_url(url)
            
            time.sleep(6)
        
        self.DA.save_reload_urls({'reload_urls':self.UM.reload_urls})    
        self.DA.save_get_urls({'get_urls':self.UM.got_urls})
        
        
if __name__ == '__main__':
    
    class_webcrawler = WebCrawler()
    class_webcrawler.main_program()
