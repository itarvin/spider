# -*- coding: utf-8 -*-
import urllib2

class Spider:
    """
        内涵段子爬虫类
    """
    def loadPage(self, page):
        """
            @brief 定义一个url请求网页的方法
            @param page 需要请求的第几页
            @returns 返回的页面html
        """

        url = "http://www.neihan8.com/article/list_5_" + str(page) + ".html"
        #User-Agent头
        user_agent = 'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT6.1; Trident/5.0'

        headers = {'User-Agent': user_agent}
        req = urllib2.Request(url, headers = headers)
        response = urllib2.urlopen(req)
        html = response.read()
        print html

        #return html