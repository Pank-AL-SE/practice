import pytest

@pytest.fixture()
def test_up(request):
    print("starting_test")
    def test_down():
        print("ending_test")
    request.addfinalizer(test_down)