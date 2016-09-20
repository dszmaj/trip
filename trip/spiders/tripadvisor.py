import scrapy
from scrapy import FormRequest
from ..items import PropertyItem


class TripadvisorSpider(scrapy.Spider):
    name = "tripadvisor"
    allowed_domains = ["tripadvisor.com"]
    common_data = {
        'seen': 0,
        'sequence': 1,
        'geo': 274723,
        'adults': 2,
        'rooms': 1,
        'searchAll': False,
        'requestingServlet': 'Hotels',
        'refineForm': True,
        'hs': None,
        'pageSize': None,
        'rad': 0,
        'dateBumped': None,
        'displayedSortOrder': 'popularity'
    }

    def start_requests(self):
        return FormRequest(
            url='https://pl.tripadvisor.com/Hotels',
            formdata=self.common_data.update({'o': 'a' + str(0)})
        )

    def parse(self, response):
        start_item = 30
        while response.status == 200:
            yield FormRequest(
                url=response.url,
                formdata=self.common_data.update({'o': 'a' + str(start_item)})
            )
            start_item += 30

        listings = response.xpath("//div[contains(concat(' ', normalize-space(@class), ' '), ' listing ')]")
        for listing in listings:
            prop = PropertyItem()
            prop.id = listing.xpath('@id').extract_first()
            prop.location = listing.xpath('@data-locationid').extract_first()
            prop.ranking = listing.xpath('@data-rankinlist').extract_first()
            prop.name = listing.xpath('//div[@class="listing_title"]/a/text()').extract_first()
            prop.url = prop.name.xpath('@href').extract_first()
            yield prop
