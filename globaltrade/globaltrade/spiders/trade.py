# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector


class TradeSpider(scrapy.Spider):
    name = 'trade'
    # allowed_domains = ['https://www.globaltrade.net/United-States/expert-service-provider.html']
    start_urls = ['https://www.globaltrade.net/expert-service-provider.html']
    page_number= 2
    def parse(self, response):
        # a=''
        next_page="https://www.globaltrade.net/United-States/expert-service-provider.html"
        # next_page=response.css('li.sp_country_71 a::attr(href)').extract()
        # print (next_page)
        # print (response.body)
        # print(a)
        yield response.follow(next_page, callback = self.page2)


    def page2(self,response):
        d=[]
        b=response.css('p.sp-name').css('a::attr(href)').extract()
        # print (b)
        # filename = 'trial1.json' 
        # with open(filename, 'a+') as f:
        #   for lis in b:
        #       f.writelines("%s\n"%lis)
        #   self.log('Saved file %s' % filename)
        # print (len(d))

        for i in b:
            s='https://www.globaltrade.net'
            news=''
            news=s+i
            yield response.follow(news,callback=self.output)
            # print(news)
        # pages='https://www.globaltrade.net/United-States/expert-service-provider.html?pageSize=10&orderBy=1&filterByPost=false&filterByRef=false&topicClear=false&industryClear=false&currentPage='+ str(TradeSpider.page_number) 
        # if TradeSpider.page_number <= 401:
        #   TradeSpider.page_number+=1
        #   yield response.follow(pages, callback=self.page2)








    def output(self,response):
        # logo=''
        # titles=''
        # sub_title=''
        # primary_location=''
        # area_of_expertise=''
        # about=''
        # website=''
        # languages_spoken=''
        # page_url=''

        # image=[]
        # image=response.css('div.image').css('img ::attr(data-original)').extract()
        # print(image)
        # logo='logourl:'+str(image[0])
        
        # titles=response.css('h1.sp-title').css('h1 ::text').extract()
        # title='title:'+str(titles[0])
        # print(title)
        # sub_titles=response.css('span.sub').css('h4 ::text').extract()
        # sub_title='sub_title:'+str(sub_titles[0])
        # print(sub_title)
        rows=response.css('div.profile-details  tr')
        # for row in rows:
        #     if response.css('td').css('span ::text').extract() == True:
        #         primary_locations=response.css('td')[1].css('span ::text').extract()
        #         primary_location='primary location:'+str(primary_locations[1])
        #         print(primary_location)
        #     if response.css('td')[1].css('a.mainExp ::text').extract()== True:
        #         area_of_expertises=response.css('td')[1].css('a.mainExp ::text').extract()
        #         area_of_expertise='area of expertise:'+str(area_of_expertises[1])
            
        #         print(area_of_expertise)





        # for row in rows[0:1]:
        #   primary_locations=response.css('td').css('span ::text').extract()
        #   primary_location='primary location:'+str(primary_locations[1])
        #   print (primary_location)

        # for row in rows[ :2]:
        #   area_of_expertises=response.css('td')[1].css('a ::text').extract()
        #   area_of_expertise='area of expertise:'+str(area_of_expertises)
        #   print (area_of_expertise)



            # print (row.extract())
        #------taking files into a list---------------
        for row in rows:
            primary_locations=[]
            primary_locations.append(response.css('td').css('td ::text').extract())
        print (len(primary_locations))
        e=primary_locations[0]
        # print(e)
        for y in e:
            print(y)

        # for delet in primary_locations:
        #     print (delet)
            # e=delet.split(',')
            # print (e)
        # print (primary_locations)
        #------------------------------------------------


        
            # area_of_expertises=response.css('td')[1].css('a.mainExp ::text').extract()
            # primary_location='primary location:'+str(primary_locations)
            # print (primary_locations)
            # print(area_of_expertises)
            # print(len(primary_locations))
                

            
            # area_of_expertises=response.css('td')[1].css('a.mainExp ::text').extract()
            # area_of_expertise='area of expertise:'+str(area_of_expertises)
            # print (area_of_expertise)
            
        # primary_locations=response.css()




        # table = response.xpath('//*[@class="profile-details"]//table')
        # row=table.xpath('//tr')
        # # print (row)
        # for row in response.xpath('//*[@class="profile-details"]//table//tr'):
        #   a=row.xpath('td[2]//text()').extract_first()
        #   b=row.xpath('td[1]//text()').extract()
        #   c=row.xpath('td[2]//text()').extract_first()
        #   d=row.xpath('td[2]//text()').extract_first()
        #   print (a)
        #   print (c)

        #   print (b[0])
        #   print(d)



        # filename = 'newfile4.html' 
        # with open(filename, 'ab') as f:
        #   f.write(response.body)
        # self.log('Saved file %s' % filename)

