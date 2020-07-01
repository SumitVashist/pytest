import pytest

@pytest.yield_fixture()
def setUptearDown():
	print("Set up method")
	yield
	print("tear Down Activity")

def test_methodA(setUptearDown):
	print("Test method A Execution")

def test_methodB(setUptearDown):
	print("Test method b Execution")