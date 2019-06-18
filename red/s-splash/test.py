import requests
from lxml import etree


def no_splash():
    url = 'https://huaban.com/boards/481662/'
    resp = requests.get(url)
    html = etree.HTML(resp.text)
    img_link = html.xpath('//div[@id="waterfall"]/div/a[contains(@class,"img")]/@href')
    print(img_link)


def use_splash():
    url = 'http://127.0.0.1:8050/'
    down = 'render.html?url=https://huaban.com/boards/481662/&wait=3&images=0'
    resp = requests.get(url+down)
    html = etree.HTML(resp.text)
    img_link = html.xpath('//div[@id="waterfall"]/div/a[contains(@class,"img")]/@href')
    print(img_link)


if __name__ == '__main__':
    no_splash()
    print("***************")
    use_splash()
