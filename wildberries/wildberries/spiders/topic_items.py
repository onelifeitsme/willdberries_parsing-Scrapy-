import scrapy
from wildberries.custom_functions import text_clear




class TopicSpider(scrapy.Spider):
    name = 'topic_items'
    start_urls = ['https://by.wildberries.ru/catalog/aksessuary/veera?sort=popular&page=1']

    def parse(self, response, **kwargs):
        item_urls = response.css('div.product-card__wrapper a::attr(href)')
        for item_url in item_urls:
            yield response.follow(item_url, callback=self.parse_product)

        for i in range(100):
            next_page = f'https://by.wildberries.ru/catalog/aksessuary/veera?sort=popular&page={i}'
            yield response.follow(next_page, callback=self.parse)


    def parse_product(self, response, **kwargs):
        brand = response.css('h1.same-part-kt__header span::text').extract()[0]
        name = response.css('h1.same-part-kt__header span::text').extract()[1]
        price = response.css('span.price-block__final-price::text').get()
        if price:
            price = text_clear(price)

        yield {
            'brand': brand,
            'name': name,
            'price': price
        }

