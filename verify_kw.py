# -*- coding: utf-8 -*-
from static import SADY, ZNAKI, WAGI


class VerifyKW(object):

    def __init__(self, number=''):
        self.number = number
        self.orginal = number

    def ck(self, sad, num):
        suma = 0
        numer = sad + num
        for nr, z in enumerate(numer[:12]):
            suma += ZNAKI[z.upper()] * WAGI[nr]
        return str(suma % 10)

    def is_valid(self):
        num_split = self.number.split('/')
        if len(num_split) == 3:
            sad, num, ck = num_split
            if sad in SADY:
                if len(num) == 8 and len(ck) == 1:
                    counkt_ck = self.ck(sad, num)
                    if counkt_ck == ck:
                        return True
        return False

    def modify(self, sad):
        self.number = self.number.replace(' ', '').replace('KW', '')
        if not self.is_valid():
            try:
                int(self.number)
            except ValueError:
                self.number = self.orginal
            else:
                num = self.number.zfill(8)
                ck = self.ck(sad, num)
                self.number = '/'.join((sad, num, ck))







