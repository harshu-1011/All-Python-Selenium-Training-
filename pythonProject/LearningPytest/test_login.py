import pytest

@pytest.mark.skip
def testlogin():
    print("Login Sucessfully")

def testlogoff():
    print("Log Out Sucessfully")

@pytest.mark.sanity
def testcalculation():
    assert 2+2==4
