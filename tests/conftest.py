import pytest


# Pytest will use rest_frameworks APIClient as its client
@pytest.fixture()
def api_client():
    from rest_framework.test import APIClient

    return APIClient()
