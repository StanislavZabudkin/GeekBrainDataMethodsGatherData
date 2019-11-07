from pprint import pprint
from lxml import html
import requests
import datetime

#header = {'user-agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) '
#                       'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 YaBrowser/19.10.2.165 (beta) Yowser/2.5 Safari/537.36'}

header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 YaBrowser/19.10.1.168 (beta) Yowser/2.5 Safari/537.36'}

headers = requests.utils.default_headers()
#headers.update(
#        {
#            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.92 YaBrowser/19.10.1.168 (beta) Yowser/2.5 Safari/537.36'
#        }
#)

#drefLenta = "//div[contains(@class,'item')]/a[./time]/text() and /.a" #|//div[@class='first-item']//h2//a/text()
##############################
# setting xpath epressions for sites lenta ru nad mail. ru
##############################
drefLenta = "//div[contains(@class,'item')]/a[./time]/time/text()|//div[contains(@class,'item')]/a[./time]/text()" #|//div[@class='first-item']//h2//a/text()
drefMainRu = "//div[contains(@class,'news-item__inner')]/a/text()|//div[contains(@class,'news-item__inner')]/a/text()"


#for $child in //Parent[@id='1']/Children/child[matches(.,"^child1","i")] return ($child/text(), $child/../../string(@name))

#//div[contains(@class,'item')]/a[./time]
itog = []


def requests_to_sites():

    req = requests.get('https://lenta.ru/',  headers=header)
    reqMailRu = requests.get('https://mail.ru/', headers=header)

    root = html.fromstring(req.text)
    rootMailRu = html.fromstring(reqMailRu.text)

#"//a[contains(@class,'link_cropped_no')]/@href|//a[contains(@class,'organic__url_type_multiline')]/@href"
#    result_list = root.xpath(drefLenta)

    genre = root.xpath(drefLenta)
    genreMairRu = rootMailRu.xpath(drefMainRu)

#    genre = root.xpath('//div[@class="rating"]/span/text()')
#    pprint(genre)

    cnout = 1

#**********************************************************
# cycles for creation
#**********************************************************
    prm = []
    for i in genre:
        pprint(i)
        if cnout%2 == 0:

            prm.append(i)
            prm.append('lentaru')
            itog.append(prm)
            prm = []
        else:
            prm.append(i+ datetime.datetime.now().strftime(" on %B %d, %Y"))
        cnout=cnout+1

    prm = []
    for i in genreMairRu:
        prm.append( datetime.datetime.now().strftime("%I:%M on %B %d, %Y"))
        prm.append(i)
        pprint(prm)
        prm.append('mailru')

        itog.append(prm)
        prm = []
        cnout=cnout+1

    print(itog)

#    for j in genreMairRu:
#        pprint(j)
#    pprint(genreMairRu)


#    if result_list:
#        for i in result_list:
#            print(i.href)
#    else:
#        print(f'{str} Not found')

requests_to_sites()
