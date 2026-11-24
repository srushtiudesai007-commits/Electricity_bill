import pytest
from electricity_bill import units_cost, fixed_charge, total_bill


def test_units_cost_slabs():
    assert units_cost(0) == 0.00
    assert units_cost(80) == 400.00      # 80 * 5
    assert units_cost(150) == 850.00     # (100 * 5) + (50 * 7)
    assert units_cost(250) == 1700.00    # (100 * 5) + (100 * 7) + (50 * 10)


def test_units_cost_negative():
    with pytest.raises(ValueError, match="cannot be negative"):
        units_cost(-10)


def test_fixed_charge():
    assert fixed_charge() == 150.00


def test_total_bill_success():
    assert total_bill(0) == 150.00
    assert total_bill(100) == 650.00     # 500 + 150
    assert total_bill(250) == 1850.00    # 1700 + 150


def test_total_bill_negative():
    with pytest.raises(ValueError, match="cannot be negative"):
        total_bill(-5)