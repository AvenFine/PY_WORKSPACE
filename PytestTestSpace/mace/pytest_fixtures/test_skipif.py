#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time : 2021/12/19 17:02
# @Author : xxx
# @FileName: test_skipif.py
# @Software: PyCharm
import pytest


@pytest.mark.skipif(condition=2 > 1, reason='tiaoguoceshi ')
def test_skipif_1():
    print('-- test_skipif_1 --')


# @pytest.mark.skipif(condition=1 == 1, reason='no jump')
def test_dkipif_2():
    print('-- case 02 --')


@pytest.mark.skipif(reason='no resason')
def test_noreason_skip():
    print('test-1')


if __name__ == '__main__':
    pytest.main(['-s', 'test_skipif.py'])