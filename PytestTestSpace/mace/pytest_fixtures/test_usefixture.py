#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time : 2021/12/19 15:37
# @Author : xxx
# @FileName: test_usefixture.py
# @Software: PyCharm
import pytest


@pytest.fixture()
def test_fix_1():
    print("---use fixture 1---")
    return 1


@pytest.fixture()
def test_fix_2(test_fix_1):
    print("fix-2")


@pytest.mark.usefixtures('test_fix_1')
def test_use_fixture():
    print("----pytest.mark.usefixtures----")


if __name__ == '__main__':
    pytest.main(['-s', 'test_usefixture.py'])