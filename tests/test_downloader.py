from downloader.downloader.spiders.images_spider import ImagesSpider


def test_get_sitemap_and_robots():
    url = 'https://test.com/path?query=test'

    sitemap, robots = ImagesSpider.get_sitemap_and_robots(url)

    assert sitemap == 'https://test.com/sitemap.xml'
    assert robots == 'https://test.com/robots.txt'
