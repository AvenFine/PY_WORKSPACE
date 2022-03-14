#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time : 2021/12/19 14:01
# @Author : xxx
# @FileName: test_scripts.py
# @Software: PyCharm
import pytest


def test_script_case01():
    print("script目录下的方法")
    assert 1111 == 1


if __name__ == '__main__':
    pytest.main()