# -*- coding: utf-8 -*-
import scrapy
from ..items import GlobaltradeItem

class TradeSpider(scrapy.Spider):
    name = 'trade'
    
    start_urls = ['https://www.globaltrade.net/expert-service-provider.html']

    
    page_number= 2
    
    def parse(self, response):
        
        next_page="https://www.globaltrade.net/United-States/expert-service-provider.html"
        
        yield response.follow(next_page, callback = self.page2)


    def page2(self,response):
        d=[]
        
        b=response.css('p.sp-name').css('a::attr(href)').extract()
        
        for i in b:
            
            s='https://www.globaltrade.net'
            news=''
            news=s+i
            
            
            yield response.follow(news,callback=self.output)
            
        pages='https://www.globaltrade.net/United-States/expert-service-provider.html?pageSize=10&orderBy=1&filterByPost=false&filterByRef=false&topicClear=false&industryClear=false&currentPage='+ str(TradeSpider.page_number) 
        if TradeSpider.page_number <= 401:
          TradeSpider.page_number+=1
          yield response.follow(pages, callback=self.page2)
    def output(self,response):
        item=GlobaltradeItem()
        
        image=response.css('div.image').css('img ::attr(data-original)').extract()
        
        item['logo']=image
        titles=response.css('h1.sp-title').css('h1 ::text').extract()
        
        item['title']=titles
        
        sub_titles=response.css('span.sub').css('span ::text').extract()
        
        item['sub_title']=sub_titles
        
        rows=response.css('div.profile-details  tr')
        for row in rows:
            primary_locations=[]
            primary_locations.append(response.css('td').css('td ::text').extract())
        
        e=primary_locations[0]
        
        for j in e:
            if j=='\n':
                e.remove(j)
            j.strip('\n')
        item['table']=e
        
        
        filename = 'results.json' 
        with open(filename, 'a+') as f:
            f.writelines(str(item))
            f.write('\n')
        self.log('Saved file %s' % filename)