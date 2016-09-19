# -*- coding: utf-8 -*-
import scrapy


class TripadvisorSpider(scrapy.Spider):
    name = "tripadvisor"
    allowed_domains = ["tripadvisor.com"]
    start_urls = (
        'https://www.tripadvisor.com/Hotels-g274723-Poland-Hotels.html',
    )

    def parse(self, response):
        pass
