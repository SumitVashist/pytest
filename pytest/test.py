import pytest

@pytest.yield_fixture()
def setUptearDown():
	print("Set up method")
	yield
	print("tear Down Activity")

@pytest.yield_fixture(scope='module')
def setUptearDownClass():
	print("Set up  Class method")
	yield
	print("tear Down Class Activity")

def test_methodA(setUptearDown,setUptearDownClass):
	print("Test method A Execution")

def test_methodB(setUptearDown,setUptearDownClass):
	print("Test method b Execution")