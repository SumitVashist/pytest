import unittest
from selenium import webdriver
import time
class GoogleSearch(unittest.TestCase):
	def setUp(self):
		global driver
		driver=webdriver.Firefox(executable_path='/home/sumit/ss/geckodriver')
		driver.get('http://google.co.in')
		driver.maximize_window()
	def test(self):
		driver.find_element_by_name('q').send_keys('Mahesh Babu')
		time.sleep(5)
		driver.find_element_by_name('btnK').click()
		driver.find_element_by_class_name('LC20lb').click()
	
	def tearDown(self):
		time.sleep(10)
		driver.close()

unittest.main()
