#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time : 2021/12/5 14:16
# @Author : xxx
# @FileName: test_param.py
# @Software: PyCharm


import pytest
from selenium import webdriver
from time import sleep


LOGINGPATH = 'http://192.168.5.102:47799/webroot/decision'


# @pytest.mark.parametrize(
#     "user, pw, expected",
#     [("1", "1", "1"),
#      ("A", 1, "B")],
#     ids=["loging_1", "login_A"])
# def test_login(user, pw, expected):
#     driver = webdriver.Chrome()
#     driver.get(LOGINGPATH)
#     driver.find_element_by_xpath(
#         "/html/body/div/div[1]/div/div[2]/div/div/div[1]/div[1]/div[1]/div[1]/div[2]/input").send_keys(user)
#     driver.find_element_by_xpath(
#         "/html/body/div/div[1]/div/div[2]/div/div/div[1]/div[2]/div[1]/div[1]/div[2]/input").send_keys(pw)
#     driver.find_element_by_id("dec-login-button").click()
#     sleep(3)
#
#     login_user = driver.find_element_by_xpath("/html/body/div/div[2]/div[2]/div[2]/div/div[2]/div").text
#
#     assert expected == login_user
#     driver.quit()


def test_hello():
    print("hello")
    assert 1 ==1


def test_fail01():
    print("01 fail")
    assert 1 == 2


def test_fail02():
    print("02 fail")
    assert 1 == 2


def test_success():
    print("03 pass")
    assert 1 == 1


def test_success1():
    print("03 pass")
    assert 1 == 1


def test_success2():
    print("03 pass")
    assert 1 == 1


def test_success3():
    print("03 pass")
    assert 1 == 1


if __name__ == '__main__':
    # pytest.main(["-s", "--maxfail=2", "test_param.py"])
    pytest.main(["-n", "2", "test_param.py"])