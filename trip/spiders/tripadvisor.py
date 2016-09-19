# -*- coding: utf-8 -*-
import scrapy


class TripadvisorSpider(scrapy.Spider):
    name = "tripadvisor"
    allowed_domains = ["tripadvisor.com"]
    start_urls = (
        'http://www.tripadvisor.com/',
    )

    def parse(self, response):
        pass
