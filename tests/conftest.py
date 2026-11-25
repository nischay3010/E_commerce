import pytest


@pytest.fixture
def expected_products():
    return {
        "Wireless Mouse": 1,
        "Bluetooth Headphones": 2,
        "Cotton T-Shirt": 3,
        "Python Crash Course": 4,
        "Basmati Rice 5kg": 5
    }