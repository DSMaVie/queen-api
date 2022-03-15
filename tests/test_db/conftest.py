import pytest


class MockMotorClient:
    def __init__(self, host, port, username, password) -> None:
        self.username = "this"


@pytest.fixture
def mock_client(scope="package"):
    return MockMotorClient


# general idea -> mock database
# db has 2 collections reachable over dot and dict notation
# both these are mock collections with async inserts bulk_writes, deletes etc.
# these raise NotImplementedErrors until I need them
