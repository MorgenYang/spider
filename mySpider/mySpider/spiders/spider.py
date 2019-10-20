import scrapy
from mySpider.items import MyspiderItem


class demoSpider(scrapy.Spider):
    name = "morgen"
    allowed_domains = ["http://www.itcast.cn"]
    start_urls = (
        'http://www.itcast.cn/channel/teacher.shtml',
    )

    def parse(self, response):
        print("morgenstart")
        print(response)
        print("morgenend")
        items = []

        for each in response.xpath("//div[@class='li_txt']"):
            item = MyspiderItem()
            name = each.xpath("h3/text()").extract()
            title = each.xpath("h4/text()").extract()
            info = each.xpath("p/text()").extract()

            item['name'] = name[0]
            item['title'] = title[0]
            item['info'] = info[0]

            items.append(item)
        return items