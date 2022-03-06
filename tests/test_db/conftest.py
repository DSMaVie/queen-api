import pytest


class MockMotorClient:
    def __init__(self, host, port, username, password) -> None:
        self.username = "this"


@pytest.fixture
def mock_client(scope="package"):
    return MockMotorClient
