import scrapy
from ..database import Property


class TripadvisorSpider(scrapy.Spider):
    name = "tripadvisor"
    allowed_domains = ["tripadvisor.com"]
    start_urls = (
        'https://www.tripadvisor.com/Hotels-g274723-Poland-Hotels.html',
    )

    def parse(self, response):
        listings = response.xpath("//div[contains(concat(' ', normalize-space(@class), ' '), ' listing ')]")
        for listing in listings:
            prop = Property()
            prop.id = listing.xpath('@id').extract_first()
            prop.location = listing.xpath('@data-locationid').extract_first()
            prop.ranking = listing.xpath('@data-rankinlist').extract_first()
            prop.name = listing.xpath('//div[@class="listing_title"]/a/text()').extract_first()
            prop.url = prop.name.xpath('@href').extract_first()
            yield prop
