import pytest
#scope=fuction,session,class,package,module
@pytest.fixture(scope="session")
def testsetUp():
    print("Launch Browser")
    print("Login")
    print("Browse The Products")
    yield
    print("Log Off")