#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time : 2021/12/19 16:23
# @Author : xxx
# @FileName: test_params.py
# @Software: PyCharm
import pytest


list_f = ['1', '2', '3']


@pytest.fixture(params=list_f)
def get_param(request):
    return request.param


def test_paracase(get_param):
    print("测试用例" + get_param)


if __name__ == '__main__':
    pytest.main(['-s', 'test_params.py'])