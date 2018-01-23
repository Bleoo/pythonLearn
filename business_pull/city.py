# -*- coding: utf-8 -*-
from business_pull.area import Area


class City:
    def __init__(self, name):
        self.name = name
        self.area = Area("")

    def set_area(self, area):
        self.area = area

    def __str__(self):
        return '{' \
               + '"city":"' + self.name + '",' \
               + '"area":' + self.area.__str__() \
               + '}'

    def __repr__(self):
        return self.__str__()