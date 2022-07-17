#!/usr/bin/env python
import csv
import time 
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Chrome



def main():

	driver = Chrome()
	driver.get("https://twitter.com/login")

	username = driver.find_element_by_xpath('//input[@name="session[username_or_email]"]')
	username.send_keys('YOUR EMAIL HERE')

	password = driver.find_element_by_xpath('//input[@name="session[password]"]')
	password.send_keys('YOUR PASSWORD HERE')

	password.send_keys(Keys.RETURN)

	search_input = driver.find_element_by_xpath('//input[@aria-label="Search query"]')
	search_input.send_keys('Gylfi Sigurdsson')
	search_input.send_keys(Keys.RETURN)

	time.sleep(3)
	cards = driver.find_elements_by_xpath('//div[@data-testid="tweet"]')
	print(len(cards))
	card = cards[0]
	print(card.find_element_by_xpath('./div[2]/div[1]//span').text)

	time_posted = card.find_element_by_xpath('.//time').get_attribute('datetime')
	print(time_posted)
	#time.sleep(5)

if __name__ == "__main__":


    main()
