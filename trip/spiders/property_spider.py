import scrapy
from scrapy import FormRequest, Request
from ..items import PropertyItem, ReviewItem


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
            self.start_item += 30
            _common = self.common_data
            _common.update({'o': 'a' + str(self.start_item)})
            yield FormRequest(
                url=response.url,
                method='POST',
                formdata=_common
            )

        listings = response.xpath("//div[contains(concat(' ', normalize-space(@class), ' '), ' listing ')]")
        for listing in listings:

            prop = PropertyItem()
            prop['id'] = listing.xpath('@id').extract_first()
            prop['location'] = listing.xpath('@data-locationid').extract_first()
            prop['ranking'] = listing.xpath('@data-rankinlist').extract_first()
            _name = listing.xpath('//*[@id="property_{}"]'.format(prop['location']))
            prop['name'] = _name.xpath('text()').extract_first()
            prop['url'] = _name.xpath('@href').extract_first()

            request = Request(
                url=response.urljoin(prop['url']),
                method='GET',
                callback=self.parse_reviews
            )
            request.meta['prop'] = prop

            yield request
            yield prop

    @staticmethod
    def parse_reviews(response):
        reviews = response.xpath("//div[contains(concat(' ', normalize-space(@class), ' '), ' reviewSelector ')]")
        for review in reviews:
            rev = ReviewItem()
            rev['id'] = review.xpath('@id').extract_first()
            _sel = review.xpath('//*[@id="{}"]'.format(rev['id']))
            rev['rating'] = _sel.xpath('//img[contains(concat(" ", normalize-space(@class), " "), " rating_s_fill ")]/@alt').extract_first()[:3]
            rev['entry'] = _sel.xpath('//p[@class="partial_entry"]/text()').extract_first()
            rev['prop'] = response.meta['prop']['id']
            yield rev

