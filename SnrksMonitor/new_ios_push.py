# coding=UTF-8
"""
author:hefeng
function:push message to ios users with the help of BARK
"""
import requests
import yaml
from log import Logger

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
            msg = "{self.push_url}{member['key']}/{message}"
            requests.get(msg)
            log.info("推送成功--{member['name']}/{msg}")

