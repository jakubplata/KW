# -*- coding: utf-8 -*-
from static import SADY, ZNAKI, WAGI


class KsiegaWieczysta(object):

    def __init__(self, numer=''):
        self.numer = numer
        self.original = numer
        self.wojewodztwo = ''
        self.powiat = ''
        self.gmina = ''
        self.miejscowosc = ''
        self.dzielnica = ''

    def ck(self, sad, num):
        suma = 0
        numer = sad + num
        for nr, z in enumerate(numer[:12]):
            suma += ZNAKI[z.upper()] * WAGI[nr]
        return str(suma % 10)

    def is_valid(self):
        num_split = self.numer.split('/')
        if len(num_split) == 3:
            sad, num, ck = num_split
            if sad in SADY:
                if len(num) == 8 and len(ck) == 1:
                    counkt_ck = self.ck(sad, num)
                    if counkt_ck == ck:
                        return True
        return False

    def modify(self, sad):
        self.numer = self.numer.replace(' ', '').replace('KW', '')
        if not self.is_valid():
            try:
                int(self.numer)
            except ValueError:
                self.numer = self.original
            else:
                num = self.numer.zfill(8)
                ck = self.ck(sad, num)
                self.numer = '/'.join((sad, num, ck))