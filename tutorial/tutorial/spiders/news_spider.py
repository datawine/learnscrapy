import scrapy

class NewsSpider(scrapy.Spider):
    name = "news"
    allowed_domains = ["news.tsinghua.edu.cn"]
    start_urls = [
        "http://news.tsinghua.edu.cn/publish/thunews/index.html"
        ]

    def parse(self, response):
        fn = "index.html"
        originindex = '/publish/thunews/index.html'
        englishindex = '/publish/thunewsen/index.html'
        with open(fn, "wb") as f:
            f.write(response.body)
        for sel in response.xpath('//ul/li/a'):
            title = sel.xpath('text()').extract();
            link = sel.xpath('@href').extract();
            if (link[0].find('publish') != -1 
                and len(title) > 0
                and link[0] != originindex
                and link[0] != englishindex):
                print title, link