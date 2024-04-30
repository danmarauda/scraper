```python
import scrapy
from scraper.items import RedditItem

class RedditSpider(scrapy.Spider):
    name = 'reddit'
    allowed_domains = ['www.reddit.com']
    start_urls = ['http://www.reddit.com/']

    def parse(self, response):
        for post in response.css('div.thing'):
            item = RedditItem()
            item['title'] = post.css('p.title a.title::text').get()
            item['url'] = post.css('p.title a.title::attr(href)').get()
            item['author'] = post.css('a.author::text').get()
            yield item

        next_page = response.css('span.next-button a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
```
