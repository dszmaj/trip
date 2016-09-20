import scrapy
from scrapy import FormRequest
from ..database import Property


class TripadvisorSpider(scrapy.Spider):
    name = "tripadvisor"
    allowed_domains = ["tripadvisor.com"]
    start_urls = (
        'https://www.tripadvisor.com/Hotels-g274723-Poland-Hotels.html',
    )
    api_url = 'https://www.tripadvisor.com/Hotels'

    def parse(self, response):
        start_item = 0
        while response.status == 200:
            yield FormRequest(
                url=self.api_url,
                formdata={
                    'seen': 0,
                    'sequence': 1,
                    'geo': 274723,
                    'adults': 2,
                    'rooms': 1,
                    'searchAll': False,
                    'requestingServlet': 'Hotels',
                    'refineForm': True,
                    'hs': None,
                    'o': 'a' + str(start_item),
                    'pageSize': None,
                    'rad': 0,
                    'dateBumped': None,
                    'displayedSortOrder': 'popularity'
                },
                callback=self.parse_api
            )
            start_item += 30

        listings = response.xpath("//div[contains(concat(' ', normalize-space(@class), ' '), ' listing ')]")
        for listing in listings:
            prop = Property()
            prop.id = listing.xpath('@id').extract_first()
            prop.location = listing.xpath('@data-locationid').extract_first()
            prop.ranking = listing.xpath('@data-rankinlist').extract_first()
            prop.name = listing.xpath('//div[@class="listing_title"]/a/text()').extract_first()
            prop.url = prop.name.xpath('@href').extract_first()
            yield prop

    def parse_api(self, response):
        pass
