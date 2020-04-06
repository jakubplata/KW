# -*- coding: utf-8 -*-

import pytest
from verify_kw import VerifyKW


def test_default_verify_kw():
    """Test that the default number is empty string"""
    vk = VerifyKW()
    assert vk.number == ''


@pytest.mark.parametrize("val,exp", [('KW 2564', 'KW2564'),
                                     ('KW  2555', 'KW2555')
                                     ])
def test_remove_spaces(val, exp):
    vk = VerifyKW(number=val)
    vk.remove_spaces()
    assert vk.number == exp


def test__is_valid():
    vk = VerifyKW(number='LD1Y/00000351/8')
    assert vk.is_valid() == True
