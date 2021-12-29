#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time : 2021/12/7 21:54
# @Author : xxx
# @FileName: test_slow.py
# @Software: PyCharm

import pytest


def test_00():
    assert 0 == 0


@pytest.mark.slow
def test_01():
    assert 1 == 1


@pytest.mark.slow
def test_02():
    assert 1 == 2


if __name__ == '__main__':
    pytest.main(["-m", "not slow", "test_slow.py"])

