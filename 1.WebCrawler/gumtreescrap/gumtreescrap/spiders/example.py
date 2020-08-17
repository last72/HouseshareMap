import scrapy


class PostSpider(scrapy.Spider):
    name = "posts"
    start_urls = [
        'https://www.gumtree.com.au/s-bicycles/ashfield-sydney/bicycle/k0c18560l3003437',
    ]

    def parse(self, response):
        for post in response.css('a.user-ad-row'):
            yield {
                'title': post.css('a.user-ad-row::text').get(),
                'price': post.css('span.user-ad-price__price::text').get(),
                'location': post.css('div.user-ad-row__location::text').get(),
                'postdate': post.css('p.user-ad-row__age::text').get(),
            }

# scrapy shell "https://www.gumtree.com.au/s-bicycles/ashfield-sydney/bicycle/k0c18560l3003437"

# Post
# post.css("a.user-ad-row::text")

# Title
# p.user-ad-row__title::text

# Price
# span.user-ad-price__price::text

# Location
# div.user-ad-row__location::text

# Post date
# p.user-ad-row__age::text
