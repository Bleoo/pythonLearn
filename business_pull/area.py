# -*- coding: utf-8 -*-

class Area:
    def __init__(self, name):
        self.name = name
        self.sub_area = ""

    def set_sub_area(self, sub_area):
        self.sub_area = sub_area

    def __str__(self):
        return '{' \
               + '"area_name":"' + self.name + '",' \
               + '"sub_area":"' + self.sub_area + '"' \
               + '}'

    def __repr__(self):
        return self.__str__()
