# -*- coding: utf-8 -*-
from grab import Grab
from lxml.html import fromstring, tostring
from inc import DBcon
import json


class Grab_inbad():
    link_in_product = []
    site = 'http://inbed.ru'
    info_xpath = {
        'title': '//div[@class="title"]/h1/text()',
        'img_link': '//div[@class="photoholder"]/div/img/@src',
        'descript': '//div[@class="descr"]/p/text()',
        'attr': '//div[@class="shortview"]//table[@class="table_goods"]'
    }
    g = Grab()
    db = DBcon.db()

    def get_link_prod(self):
        page = 0
        while page >= 0:
            resp = self.g.go(self.site + '/?ajax=prodlistprods&page=' + str(page))
            resp = resp.body.decode('utf-8')
            html = json.loads(resp)['html']
            if len(html) <= 0:
                break
            #if page == 1:
            #    break
            print(page)
            try:
                data = fromstring(html).xpath('//div[@class="prod_holder"]/a/@href')
            except Exception:
                break
            print(data)
            self.link_in_product.extend(data)
            page = page + 1

    def get_info_product(self):
        for param in self.link_in_product:
            print(param)
            resp = self.g.go(self.site + param)
            html = resp.body.decode('utf-8')
            prodditail = fromstring(html).xpath('//div[@class="proddetail"]')
            if len(prodditail[0].xpath(self.info_xpath['descript'])) > 0:
                descript = prodditail[0].xpath(self.info_xpath['descript'])
            else:
                descript = ' '
            if len(prodditail[0].xpath(self.info_xpath['title'])) > 0:
                title = prodditail[0].xpath(self.info_xpath['title'])
            else:
                title = ' '
            if len(prodditail[0].xpath(self.info_xpath['img_link'])) > 0:
                img = prodditail[0].xpath(self.info_xpath['img_link'])[0]
            else:
                img = ' '
            item = {
                'title': title,
                'descript': descript,
                'img': img
            }

            prod_attr = prodditail[0].xpath(self.info_xpath['attr'])
            item['attr'] = tostring(prod_attr[0], pretty_print=True, encoding='utf-8').decode('utf-8')
            #print(item)
            self.db.inser_data(item)




