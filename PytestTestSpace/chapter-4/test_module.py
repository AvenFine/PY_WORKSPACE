#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time : 2021/11/15 22:00
# @Author : xxx
# @FileName: test_module.py
# @Software: PyCharm


def test_ehlo(smtp_connection):
    response, _ = smtp_connection.ehlo()
    smtp_connection.extra_attr = 'test'
    assert 0  # 为了展示，强制失败


def test_noop(smtp_connection):
    response, _ = smtp_connection.noop()
    assert response == 250
    assert smtp_connection.extra_attr == 0   # 强制失败


