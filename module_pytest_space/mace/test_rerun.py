#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time : 2021/12/7 22:07
# @Author : xxx
# @FileName: test_rerun.py
# @Software: PyCharm


import pytest


def test_01():
    assert 1 == 2


def test_02():
    assert 1 == 3


if __name__ == '__main__':
    pytest.main(["--reruns", "5", "--reruns-delay", "1", "test_rerun.py"])
