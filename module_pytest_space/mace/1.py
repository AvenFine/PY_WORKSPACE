#!/usr/bin/python3
# -*- coding: utf-8 -*-

# @Time : 2021/12/5 14:51
# @Author : xxx
# @FileName: 1.py
# @Software: PyCharm

from selenium import webdriver
from time import sleep


driver = webdriver.Chrome()
driver.get('http://192.168.5.102:47799/webroot/decision')
sleep(1)
driver.find_element_by_xpath("/html/body/div/div[1]/div/div[2]/div/div/div[1]/div[1]/div[1]/div[1]/div[2]/input").send_keys(1)
driver.find_element_by_xpath("/html/body/div/div[1]/div/div[2]/div/div/div[1]/div[2]/div[1]/div[1]/div[2]/input").send_keys(1)
driver.find_element_by_id("dec-login-button").click()
