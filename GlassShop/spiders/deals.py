# -*- coding: utf-8 -*-
import scrapy


class DealsSpider(scrapy.Spider):
    name = 'deals'
    allowed_domains = ['www.glassesshop.com']
    start_urls = ['https://www.glassesshop.com/bestsellers']

    def parse(self, response):
        for glass in response.xpath('//div[@class="prlist row"]/div[@class="col-sm-6 col-md-4 m-p-product"]'):
            yield {
                'url': glass.xpath(".//div[@class='pimg default-image-front']/a/@href").get(),
                'img_url': glass.xpath(".//div[@class='pimg default-image-front']/a/img[@src][1]").get(),
                'title': glass.xpath(".//div[@class='row']/p[@class='pname col-sm-12']/a/text()").get()

            }
