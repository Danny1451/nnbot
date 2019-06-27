# -*- coding: UTF-8 -*-
"""
author:hefeng
function:push message to ios users with the help of BARK
"""
import requests
import yaml
from log import Logger
import time
 
log = Logger().log()


class PushToIos:
    def __init__(self):
        self.push_url = "https://api.day.app/"
        self.push_list = [
            {
                "key": 'HQ92qeFotCGhWvo4j8BJCW',
                "name": "Max"
            },
            {
                "key":"nBZbFqaDWmqZcxdYi8ds8W",
                "name":"6sp"
            }
        ]


    def push(self, message):
        for member in self.push_list:
            msg =u"{}{}/{}".format(self.push_url,member['key'],message)
            # msg = "{self.push_url}{member['key']}/{message}"
            requests.get(msg)
            log.info(u"推送成功--{} : {}".format(member['name'],''))

    def notifyUpdateInfo(self, datas):
        timeStr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
        log.info(datas)
        msg = u"{}/ 🚀 {} 🤓 {} 🥳 Detect Time:{}".format(datas['title'],datas['reason'],datas['info'],timeStr)
        self.push(msg)

if __name__ == '__main__':
    pt = PushToIos()
    shoeDict = [{
                    'title': 'Nike x Stranger Things Air Tailwind 79 123',
                    'info': '2019-06-27 09:00:00',
                    'reason': 'MerchStatus Update'
                }]
    pt.notifyUpdateInfo(shoeDict)
    # msg ='{}{}/{}'.format('🐶','🐶','🐶')
    # pt.push(u"Nike x Stranger Things Air Tailwind 79 123 🤓 2019-06-27 09:00:00 info MerchStatus Update")

