from __future__ import annotations
from decimal import Decimal, ROUND_HALF_UP


def _to_decimal(value: float | int | str | Decimal) -> Decimal:
    return Decimal(str(value))


def _round_currency(amount: Decimal) -> float:
    return float(amount.quantize(Decimal("0.01"), rounding=ROUND_HALF_UP))


def units_cost(units: float | int | str | Decimal) -> float:
    """Calculate tiered electricity consumption cost based on units used."""
    u = _to_decimal(units)

    if u < 0:
        raise ValueError("Units consumed cannot be negative.")

    if u <= Decimal("100"):
        cost = u * Decimal("5.00")
    elif u <= Decimal("200"):
        cost = (Decimal("100") * Decimal("5.00")) + ((u - Decimal("100")) * Decimal("7.00"))
    else:
        cost = (
            (Decimal("100") * Decimal("5.00"))
            + (Decimal("100") * Decimal("7.00"))
            + ((u - Decimal("200")) * Decimal("10.00"))
        )

    return _round_currency(cost)


def fixed_charge() -> float:
    """Return the standard monthly fixed meter/connection charge."""
    return _round_currency(Decimal("150.00"))


def total_bill(units: float | int | str | Decimal) -> float:
    """Calculate the total electricity bill (units cost + fixed charge)."""
    usage = _to_decimal(units_cost(units))
    fixed = _to_decimal(fixed_charge())
    return _round_currency(usage + fixed)


if __name__ == "__main__":
    consumed_units = 250
    final_amount = total_bill(consumed_units)
    print(f"Total Electricity Bill for {consumed_units} units: {final_amount:.2f}")