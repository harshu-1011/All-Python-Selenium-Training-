import pytest


@pytest.mark.parametrize("a,b,final,d",[(2,3,5,"Hello"),(1,3,4,"Raj"),(3,5,8,"Harshu")])
def test_add(a,b,final,d):
    print(d)
    assert a + b == final


