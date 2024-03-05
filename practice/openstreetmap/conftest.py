import pytest

@pytest.fixture(autouse=True)
def test_up(request):
    print("\nstarting_test")
    yield
    print("\nending_test")
    