import scrapy


class TopicSpider(scrapy.Spider):
    name = 'topic'
    allowed_domains = ['https://by.wildberries.ru/']
    start_urls = ['http://https://by.wildberries.ru//']

    def parse(self, response):
        pass
