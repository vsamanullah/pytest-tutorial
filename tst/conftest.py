import pytest

@pytest.fixture(autouse=True)
def method_scope():
    print("executed per function before the function")
    yield
    print("executed per function after the function")


@pytest.fixture(scope="class")
def class_scope():
    print("executed per class")

@pytest.fixture(scope="module")
def module_scope():
    print("executed per per module")

@pytest.fixture(scope="session")
def session_scope():
    print("executed per per session")



