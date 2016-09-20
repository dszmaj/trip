import scrapy
from scrapy import FormRequest
from ..items import PropertyItem


class PropertySpider(scrapy.Spider):
    name = "tripadvisor"
    allowed_domains = ["tripadvisor.com"]
    common_data = {
        'seen': '0',
        'sequence': '1',
        'geo': '274723',
        'adults': '2',
        'rooms': '1',
        'searchAll': 'false',
        'requestingServlet': 'Hotels',
        'refineForm': 'true',
        'hs': '',
        'pageSize': '',
        'rad': '0',
        'dateBumped': '',
        'displayedSortOrder': 'popularity'
    }
    start_item = 0

    def start_requests(self):
        _common = self.common_data
        _common.update({'o': 'a' + str(0)})
        return [FormRequest(
            url='https://pl.tripadvisor.com/Hotels',
            method='POST',
            formdata=_common
        )]

    def parse(self, response):
        if response.status == 200:
            _common = self.common_data
            _common.update({'o': 'a' + str(self.start_item)})
            yield FormRequest(
                url=response.url,
                method='POST',
                formdata=_common
            )
            self.start_item += 30

        listings = response.xpath("//div[contains(concat(' ', normalize-space(@class), ' '), ' listing ')]")
        for listing in listings:
            prop = PropertyItem()
            prop['id'] = listing.xpath('@id').extract_first()
            prop['location'] = listing.xpath('@data-locationid').extract_first()
            prop['ranking'] = listing.xpath('@data-rankinlist').extract_first()
            _name = listing.xpath('//*[@id="property_{}"]'.format(prop['location']))
            prop['name'] = _name.xpath('text()').extract_first()
            prop['url'] = _name.xpath('@href').extract_first()
            yield prop
