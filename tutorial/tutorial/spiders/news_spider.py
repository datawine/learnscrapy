import scrapy

class NewsSpider(scrapy.Spider):
    name = "news"
    allowed_domains = ["news.tsinghua.edu.cn"]
    start_urls = [
        "http://news.tsinghua.edu.cn/publish/thunews/index.html"
        ]

    def parse(self, response):
        fn = "index.html"
        with open(fn, "wb") as f:
            f.write(response.body)