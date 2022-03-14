#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time : 2021/12/19 15:18
# @Author : xxx
# @FileName: test_fixtre_02.py
# @Software: PyCharm
import pytest


# fixture嵌套使用fixture
@pytest.fixture()
def first_case():
    return "ab"


@pytest.fixture()
def order_case(first_case):
    return [first_case]


def test_list(order_case):
    order_case.append("b")
    assert order_case == ["a", "b"]


if __name__ == '__main__':
    pytest.main(["-s", "test_fixtre_02.py"])



