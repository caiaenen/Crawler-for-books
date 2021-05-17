import requests
import re
from lxml import etree

str1 = input("请输入资源名称：")
hds=[
    {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.1.6) Gecko/20091201 Firefox/3.5.6'},
    {'User-Agent':'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11'},
    {'User-Agent': 'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0)'}]

def getUrls():
    url = 'http://www.yunxs.com/' + str1
    response = requests.get(url=url, headers=hds[page_num%len(hds)])
    print(response.encoding,'22',response.apparent_encoding)

    response.encoding = response.apparent_encoding
    data = etree.HTML(response.text)
    a_list = data.xpath('//div[@class="list_box"]//ul/li/a')
    print(a_list)
    a_urls = []
    for a in a_list:
        a_url = url+a.xpath('./@href')[0]
        a_urls.append(a_url)
    return a_urls


def get_text(url):
    response = requests.get(url)
    print(response.encoding, '22', response.apparent_encoding)
    response.encoding = response.apparent_encoding
    content = response.text

    clear = re.compile('<\s*script[^>]*>[^<]*<\s*/\s*script\s*>', re.I)
    t = clear.sub('', content)
    t = re.sub('<br>', '\r',t)
    data = etree.HTML(t)
    text1 = data.xpath('//div[@class="box_box"]')[0].xpath('string(.)')
    print(text1)
    return text1

def write_to_my():
    a_urls = getUrls()
    book = ''
    for url in a_urls:
        book = book + (get_text(url))
        # print(get_text(url))
    with open(r".\daai.doc", 'w', encoding="utf-8") as file:
        file.write(book)


write_to_my()