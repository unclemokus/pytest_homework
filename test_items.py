#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 16:20:50 2019

@author: io
"""

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_login_link_pass(browser):
    browser.get(link)
    button = browser.find_element_by_class_name("btn.btn-lg.btn-primary.btn-add-to-basket")
    button.click()
    x = browser.find_element_by_xpath("(//div[@class='alertinner '])[1]")
    assert x, "Товар не добавлен в корзину"

