import os
import re

import scrapy

from tutorial.items import NewsItem


def genNewsItem(title, link):
    nitem = NewsItem()
    nitem['title'] = title
    nitem['link'] = link
    return nitem

class NewsSpider(scrapy.Spider):
    name = "news"
    allowed_domains = ["news.tsinghua.edu.cn"]
    start_urls = [
        "http://news.tsinghua.edu.cn/publish/thunews/index.html"
        ]

    def parse(self, response):
        fn = "index.html"
        baseurl = 'http://news.tsinghua.edu.cn'
        originindex = '/publish/thunews/index.html'
        englishindex = '/publish/thunewsen/index.html'
        with open(fn, "wb") as f:
            f.write(response.body)
        for sel in response.xpath('//ul/li/a'):
            title = sel.xpath('text()').extract();
            link = sel.xpath('@href').extract();
            if (link[0].find('publish') != -1 and len(title) > 0
                and link[0] != originindex and link[0] != englishindex):
                pageurl = baseurl + link[0]
                yield scrapy.Request(pageurl, callback=self.pasePage)
    
    def pasePage(self, response):
        fn =  response.xpath('//title').extract()[0]
        fn = re.split('[<>]', fn)
        fn = fn[2].replace(' ', '').split('-')[1]
        os.makedirs('./newsdata/' + fn)
        with open('./newsdata/' + fn + '/' + fn + '.html', 'wb') as f:
            f.write(response.body)
