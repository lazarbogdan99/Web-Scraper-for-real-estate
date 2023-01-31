import scrapy
import re

class ApartmentsSpider(scrapy.Spider):
    name = 'apartments'
    start_urls = ['https://www.imobiliare.ro/vanzare-apartamente/bucuresti-ilfov?id=82493726']


    

    def parse(self, response):
        for apartments in response.css('div.col_descriere'):
            yield {
                'name': re.sub('<.*?>', '',apartments.css('h2.titlu-anunt span').get()).strip(),
                'location':apartments.css('p.location_txt span::text').get().strip().replace('ş','s'),
                'rooms':apartments.css('div.swiper-slide:first-child span strong::text').get(),
                'area':apartments.css('div.swiper-slide:nth-child(2) span strong::text').get(),
                'floor':apartments.css('div.swiper-slide:nth-child(3) span strong::text').get(),
                'type':apartments.css('div.swiper-slide:last-child span strong::text').get(),
                'price':apartments.css('span.pret-mare::text').get(),        
        } 
        next_page = response.css('a.inainte.butonpaginare').attrib['href']
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
        else: print("No more pages")