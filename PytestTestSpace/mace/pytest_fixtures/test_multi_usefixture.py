#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time : 2021/12/19 15:49
# @Author : xxx
# @FileName: test_multi_usefixture.py
# @Software: PyCharm
import pytest


@pytest.fixture()
def fix1():
    print("-- fix1 --")


@pytest.fixture()
def fix2():
    print("-- fix2 --")


@pytest.mark.usefixtures('fix1')
@pytest.mark.usefixtures('fix2')
def test_usefix():
    print('func_usefix')


@pytest.mark.usefixtures('fix2')
@pytest.mark.usefixtures('fix1')
class Test_c_usefix():
    def test_fix1(self):
        print('--class/fix1--')

    def test_fix2(self):
        print('--class/fix2--')


if __name__ == '__main__':
    pytest.main(['-s', 'test_multi_usefixture.py'])