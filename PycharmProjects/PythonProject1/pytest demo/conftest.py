import pytest

# @pytest.fixture(scope="class")
@pytest.fixture
def setup():
    print("Setting up the test environment")
    yield
    print("Tearing down the test environment")

@pytest.fixture
def dataload():
    print("User profile is being created")
    return["Sumit","Sinha","sumitkumarsinha1992@gmail.com"]