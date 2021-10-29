from copy import deepcopy
from furl import furl
from downloader.items import ImageItem
import scrapy


class ImagesSpider(scrapy.Spider):
    name = 'images'

    def __init__(self, url=None, *args, **kwargs):
        super(ImagesSpider, self).__init__(*args, **kwargs)
        self.start_url = url
        self.start_urls = [url]

    def parse(self, response, **kwargs):
        # Parse other urls
        yield from self.get_callbacks(response)
        # Download files
        yield from self.get_files(response)

    def get_files(self, response):
        """
        Parse urls from src attributes of img html tags and return items to download
        """

        urls = response.css('img::attr(src)').getall()
        for url in urls:
            url = response.urljoin(url)
            yield ImageItem(image_urls=[url])

    def get_callbacks(self, response):
        """
        Parse links and return new requests
        """

        links = response.css('a::attr(href)').getall()
        for link in links:
            link = response.urljoin(link)

            if furl(link).host == furl(self.start_url).host:
                yield scrapy.Request(link, callback=self.parse)

    @staticmethod
    def get_sitemap_and_robots(url: str):
        url = furl(url)

        url.set(query=None)
        robots = deepcopy(url).set(path='robots.txt')
        sitemap = deepcopy(url).set(path='sitemap.xml')

        return sitemap.url, robots.url
