import re

from scrapy.selector import Selector
from android_apps_crawler.items import AppItem

def parse_anzhi(response):
    xpath = "//div[@class='app_detail']"
    xpath_name = "//div[@class='detail_description']/div/h3/text()"
    xpath_version = "//span[@class='app_detail_version']/text()"
    xpath_url = "//div[@class='detail_down']/a/@onclick"
    appItemList = []
    sel = Selector(response)
    for detail in sel.xpath(xpath).extract():
        sel_inner = Selector(text=detail)
        appItem = AppItem()
        for app_name in sel_inner.xpath(xpath_name).extract():
            appItem['app_name'] = app_name

        for app_version in sel_inner.xpath(xpath_version).extract():
            if app_version.startswith('(') and app_version.endswith(')'):
                appItem['version'] = app_version[1:-1]

        for download_script in sel_inner.xpath(xpath_url).extract():
            id = re.search(r"\d+", download_script).group()
            url = "http://www.anzhi.com/dl_app.php?s=%s&n=5" % (id,)
            appItem['url'] = url

        appItemList.append(appItem)

    return appItemList

