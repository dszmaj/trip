from scrapy.crawler import CrawlerProcess

from trip.spiders.tripadvisor import PropertySpider


if __name__ == '__main__':
    process = CrawlerProcess({
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
        'DOWNLOAD_DELAY': 3,
        'CONCURRENT_REQUESTS_PER_DOMAIN': 3,
        'COOKIES_ENABLED': False,
        'TELNETCONSOLE_ENABLED': False,
        'DEFAULT_REQUEST_HEADERS': {
            'Accept': 'text/javascript, text/html, application/xml, text/xml, */*',
            'Accept-Language': 'pl-PL,pl;q=0.8,en-US;q=0.6,en;q=0.4',
            'Referer': 'https://pl.tripadvisor.com/Hotels-g274723-Poland-Hotels.html',
            'DNT': 1,
            'X-Requested-With': 'XMLHttpRequest',
            'X-Puid': 'V@EpKQokKXsAAOswUMgAAAAu',
            'Connection': 'keep-alive',
            'Host': 'pl.tripadvisor.com'
        },
        'ITEM_PIPELINES': {
            #'trip.pipelines.SomePipeline': 300,
        }
    })

    process.crawl(PropertySpider)
    process.start()
