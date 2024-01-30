import pytest

@pytest.fixture(params=["a","b"])
def test_add(request):
    print(request.param)

def test_display(test_add):
    print("Display is Called")