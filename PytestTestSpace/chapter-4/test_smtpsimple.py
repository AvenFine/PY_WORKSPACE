#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time : 2021/11/20 16:37
# @Author : xxx
# @FileName: test_smtpsimple.py
# @Software: PyCharm


def test_ehlo_yield(smtp_connection_yield):
    response, _ = smtp_connection_yield.ehlo()
    assert response == 250
    assert 0