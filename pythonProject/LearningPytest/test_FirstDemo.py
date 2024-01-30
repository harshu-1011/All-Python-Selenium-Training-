import pytest
@pytest.mark.filterwarnings
def testlogin():
    print("Login Sucessfully")

@pytest.mark.sanity
def testlogoff():
    print("Log Out Sucessfully")

def testcalculation():
    assert 2+2==4
