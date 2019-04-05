# -*- coding: utf-8 -*-
import scrapy



class TradeSpider(scrapy.Spider):
    name = 'trade'
    
    start_urls = ['https://www.globaltrade.net/expert-service-provider.html']
    page_number= 2
    u=0
    def parse(self, response):
        # a=''
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
        logo=''
        titles=''
        sub_title=''
        primary_location=''
        area_of_expertise=''
        about=''
        website=''
        languages_spoken=''
        page_url=''

        image=[]
        image=response.css('div.image').css('img ::attr(data-original)').extract()
        
        logo='logourl:'+str(image[0])
        
        titles=response.css('h1.sp-title').css('h1 ::text').extract()
        title='title:'+str(titles[0])
        
        sub_titles=response.css('span.sub').css('span ::text').extract()
        sub_title='sub_title:'+str(sub_titles[0])
        
        rows=response.css('div.profile-details  tr')





        


        
        for row in rows:
            primary_locations=[]
            primary_locations.append(response.css('td').css('td ::text').extract())
        
        e=primary_locations[0]
        
        filename = 'trial%d.json'%TradeSpider.u 
        with open(filename, 'a+') as f:
        
              f.writelines("%s\n"%logo)
              f.writelines("%s\n"%title)
              f.writelines("%s\n"%sub_title)
              f.writelines(e)
        self.log('Saved file %s' % filename)
        TradeSpider.u+=1
        
