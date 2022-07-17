#!/usr/bin/env python


from selenium import webdriver

url = "https://www.premierleague.com/players/4640/Jordan-Pickford/stats?co=1&se=363"

driver = webdriver.Chrome()
driver.get(url)