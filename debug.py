from scrapy.crawler import CrawlerProcess

from .trip.spiders.tripadvisor import TripadvisorSpider


if __name__ == '__main__':
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)',
        'DOWNLOAD_DELAY': 3,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 3,
        'COOKIES_ENABLED': False,
        'TELNETCONSOLE_ENABLED': False,
        'DEFAULT_REQUEST_HEADERS': {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
            'Accept-Language': 'pl',
        },
        'ITEM_PIPELINES': {
            'trip.pipelines.SomePipeline': 300,
        }
    })

    process.crawl(TripadvisorSpider)
    process.start()
