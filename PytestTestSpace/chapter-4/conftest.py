#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time : 2021/11/15 21:57
# @Author : xxx
# @FileName: conftest.py.py
# @Software: PyCharm

import pytest
import smtplib


@pytest.fixture(scope='module')
def smtp_connection():
    return smtplib.SMTP("smtp.163.com", 25, timeout=5)


@pytest.fixture(scope='package')
def smtp_connection_package():
    return smtplib.SMTP("smtp.163.com", 25, timeout=5)


@pytest.fixture()
def smtp_connection_yield():
    smtp_connection = smtplib.SMTP("smtp.163.com", 25, timeout=5)
    yield smtp_connection
    print("关闭SMTP连接")
    smtp_connection.close()