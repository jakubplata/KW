# -*- coding: utf-8 -*-

import pytest
from ksiega_wieczysta import KsiegaWieczysta
from dzialka import Dzialka


def test_default_verify_kw():
    """Test that the default number is empty string"""
    vk = KsiegaWieczysta()
    assert vk.numer == ''


@pytest.mark.parametrize("val,exp", [('LD1Y/00000351/8', True), ('KW  2555', False), ('JD1Y/00000351/8', False),
                                     ('LD1Y/00000351/5', False), ('LD1Y/0000351/5', False), ('test', False)
                                     ])
def test_is_valid(val, exp):
    vk = KsiegaWieczysta(numer=val)
    assert vk.is_valid() == exp


@pytest.mark.parametrize("val,exp", [('KW  2555', 'LD1Y/00002555/2'), ('KW LD1Y/00000351/8', 'LD1Y/00000351/8'),
                                     ('ZD 2564', 'ZD 2564')])
def test_modify(val, exp):
    vk = KsiegaWieczysta(numer=val)
    vk.modify('LD1Y')
    assert vk.numer == exp


def test_clar_dzialki():
    vk = KsiegaWieczysta(numer='LD1Y/00002555/2')
    for i in ['', '//', '---', '100', '200']:
        d = Dzialka()
        d.numer = i
        vk.dzialki.append(d)
    vk.clear_dzialki()
    assert len(vk.dzialki) == 2
    for dz in vk.dzialki:
        assert dz.numer in ['100', '200']