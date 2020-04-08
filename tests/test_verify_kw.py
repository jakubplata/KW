# -*- coding: utf-8 -*-

import pytest
from verify_kw import VerifyKW


def test_default_verify_kw():
    """Test that the default number is empty string"""
    vk = VerifyKW()
    assert vk.number == ''


@pytest.mark.parametrize("val,exp", [('LD1Y/00000351/8', True), ('KW  2555', False), ('JD1Y/00000351/8', False),
                                     ('LD1Y/00000351/5', False), ('LD1Y/0000351/5', False), ('test', False)
                                     ])
def test_is_valid(val, exp):
    vk = VerifyKW(number=val)
    assert vk.is_valid() == exp


@pytest.mark.parametrize("val,exp", [('KW  2555', 'LD1Y/00002555/2'), ('KW LD1Y/00000351/8', 'LD1Y/00000351/8'),
                                     ('ZD 2564', 'ZD 2564')])
def test_modify(val, exp):
    vk = VerifyKW(number=val)
    vk.modify('LD1Y')
    assert vk.number == exp