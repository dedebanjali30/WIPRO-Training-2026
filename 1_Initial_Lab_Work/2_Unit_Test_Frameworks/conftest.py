import pytest


@pytest.fixture
def sample_data():
    return {
        "username": "admin",
        "password": "admin123"
    }