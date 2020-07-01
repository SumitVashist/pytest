"""
Both setUpclass(cls) and tearDown(cls) method will execute only one time and 
and other method will be executed for every test


"""


import unittest as ut

class TestCaseDemo(ut.TestCase):
	@classmethod
	def setUpClass(cls):
		print("Setup class method execution")


	def setUp(self):
		print("Setup method Execution ... ")

	def test1(self):
		print("test method 1 Execution .. ")


	def test2(self):
		print("test method 2 Execution .. ")

	def tearDown(self):
		print("Tear Down method Execution .. ")


	@classmethod
	def tearDownClass(cls):
		print("Tear down class method execution")

ut.main()
