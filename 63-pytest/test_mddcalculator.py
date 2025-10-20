import pytest
from mddcalculator import calc_mdd


# Fixture: common sample price list for testing
@pytest.fixture
def sample_prices():
    # This fixture returns a predefined test case of prices.
    return [100, 90, 80, 110, 100, 85]


# Parametrized test for various cases
@pytest.mark.parametrize(
    "prices, expected",
    [
        ([100], 0),  # Single price: no drawdown.
        ([10, 20, 30, 40], 0),  # Strictly increasing: no drawdown.
        ([40, 30, 20, 10], 30),  # Strictly decreasing: drawdown = 30.
        ([100, 90, 80, 110, 100, 85], 25),  # Fluctuating: maximum drawdown = 25.
        ([100, 100, 100], 0),  # Constant: drawdown = 0.
    ],
)
def test_calc_mdd(prices, expected):
    # Test that calc_mdd returns the expected maximum drawdown.
    assert calc_mdd(prices) == pytest.approx(expected)


# Additional test using a fixture
def test_calc_mdd_with_fixture(sample_prices):
    # Using the sample_prices fixture; expected maximum drawdown is 25.
    expected = 25
    assert calc_mdd(sample_prices) == pytest.approx(expected)
