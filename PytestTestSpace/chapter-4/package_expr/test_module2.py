#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time : 2021/11/15 22:11
# @Author : xxx
# @FileName: test_module2.py
# @Software: PyCharm

def test_ehlo_in_module2(smtp_connection_package):
    response, _ = smtp_connection_package.ehlo()
    assert response == 250
    assert 0