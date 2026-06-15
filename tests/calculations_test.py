# System Modules
import sys
import os
import math

# Installed Modules
import pytest

# Project Modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from calculations import (   # noqa: E402
    area_of_circle,
    area_of_circle_in_unit,
    get_nth_fibonacci,
    ShapeOptions,
    Geometry,
    Owner,
)


def test_area_of_circle_positive_radius():
    """Test with a positive radius."""
    # Arrange
    radius = 1

    # Act
    result = area_of_circle(radius)

    # Assert
    assert abs(result - math.pi) < 1e-10


def test_area_of_circle_zero_radius():
    """Test with a radius of zero."""
    # Arrange
    radius = 0

    # Act
    result = area_of_circle(radius)

    # Assert
    assert result == 0


def test_area_of_circle_negative_radius():
    """Test with a negative radius."""
    # Arrange
    radius = -1

    # Act & Assert
    with pytest.raises(ValueError, match="Radius cannot be negative"):
        area_of_circle(radius)


def test_get_nth_fibonacci_zero():
    """Test with n=0."""
    # Arrange
    n = 0

    # Act
    result = get_nth_fibonacci(n)

    # Assert
    assert result == 0


def test_get_nth_fibonacci_one():
    """Test with n=1."""
    # Arrange
    n = 1

    # Act
    result = get_nth_fibonacci(n)

    # Assert
    assert result == 1


def test_get_nth_fibonacci_ten():
    """Test with n=10."""
    # Arrange
    n = 10

    # Act
    result = get_nth_fibonacci(n)

    # Assert
    assert result == 55


def test_get_nth_fibonacci_negative():
    """Test with negative n."""
    # Arrange
    n = -1

    # Act & Assert
    with pytest.raises(ValueError, match="n cannot be negative"):
        get_nth_fibonacci(n)


def test_area_of_circle_in_unit_meters():
    """Test area in square meters."""
    # Arrange
    radius = 2

    # Act
    result = area_of_circle_in_unit(radius, "m")

    # Assert
    assert abs(result - math.pi * 4) < 1e-10


def test_area_of_circle_in_unit_cm():
    """Test area converted to square centimeters."""
    # Arrange
    radius = 2

    # Act
    result = area_of_circle_in_unit(radius, "cm")

    # Assert
    assert abs(result - math.pi * 4 * 10_000) < 1e-5


def test_area_of_circle_in_unit_mm():
    """Test area converted to square millimeters."""
    # Arrange
    radius = 2

    # Act
    result = area_of_circle_in_unit(radius, "mm")

    # Assert
    assert abs(result - math.pi * 4 * 1_000_000) < 1


def test_area_of_circle_in_unit_negative():
    """Test that a negative radius raises an error for any unit."""
    # Arrange
    radius = -1

    # Act & Assert
    with pytest.raises(ValueError, match="Radius cannot be negative"):
        area_of_circle_in_unit(radius, "cm")


def _make_owner():
    return Owner(
        first_name="João",
        last_name="Silva",
        email="joao@example.com",
        phone="99999-9999",
        address="Rua A, 123",
        city="Recife",
        state="PE",
    )


def _make_geometry():
    """Helper that builds a Geometry instance for the tests."""
    return Geometry(name="figuras", owner=_make_owner())


def test_geometry_process_shape_rectangle():
    """process_shape should compute a simple rectangle area."""
    # Arrange
    geometry = _make_geometry()

    # Act
    result = geometry.process_shape(
        "rectangle", 2, 3, 0, 0, 0,
        options=ShapeOptions(unit="m", scale=1, precision=2,
                             should_print=False, should_round=True,
                             should_validate=True, tax_rate=0),
    )

    # Assert
    assert result == 6
    assert geometry.shapes == [6]


def test_geometry_process_shape_circle_with_unit_and_tax():
    """process_shape should apply unit conversion and tax rate."""
    # Arrange
    geometry = _make_geometry()

    # Act
    result = geometry.process_shape(
        "circle", 1, 0, 0, 0, 0,
        options=ShapeOptions(unit="cm", scale=1, precision=4,
                             should_print=False, should_round=True,
                             should_validate=True, tax_rate=10),
    )

    # Assert
    expected = round(math.pi * 10_000 * 1.10, 4)
    assert result == expected


def test_geometry_process_shape_validation_error():
    """process_shape should reject negative dimensions when validating."""
    # Arrange
    geometry = _make_geometry()

    # Act & Assert
    with pytest.raises(ValueError, match="No negatives allowed"):
        geometry.process_shape(
            "rectangle", -1, 3, 0, 0, 0,
            options=ShapeOptions(unit="m", scale=1, precision=2,
                                 should_print=False, should_round=False,
                                 should_validate=True, tax_rate=0),
        )


def test_geometry_process_shape_triangle():
    """process_shape should compute a triangle area."""
    # Arrange
    geometry = _make_geometry()

    # Act
    result = geometry.process_shape(
        "triangle", 4, 3, 0, 0, 0,
        options=ShapeOptions(unit="m", scale=1, precision=2,
                             should_print=False, should_round=True,
                             should_validate=False, tax_rate=0),
    )

    # Assert
    assert result == 6


def test_geometry_process_shape_trapezoid():
    """process_shape should compute a trapezoid area."""
    # Arrange
    geometry = _make_geometry()

    # Act
    result = geometry.process_shape(
        "trapezoid", 2, 4, 5, 0, 0,
        options=ShapeOptions(unit="m", scale=1, precision=2,
                             should_print=False, should_round=True,
                             should_validate=False, tax_rate=0),
    )

    # Assert
    assert result == 15


def test_geometry_process_shape_box():
    """process_shape should compute a box volume."""
    # Arrange
    geometry = _make_geometry()

    # Act
    result = geometry.process_shape(
        "box", 2, 3, 4, 0, 0,
        options=ShapeOptions(unit="m", scale=1, precision=2,
                             should_print=False, should_round=True,
                             should_validate=False, tax_rate=0),
    )

    # Assert
    assert result == 24


def test_geometry_process_shape_weird_with_mm_unit():
    """process_shape should sum dimensions and convert to mm."""
    # Arrange
    geometry = _make_geometry()

    # Act
    result = geometry.process_shape(
        "weird", 1, 2, 3, 4, 5,
        options=ShapeOptions(unit="mm", scale=1, precision=2,
                             should_print=False, should_round=True,
                             should_validate=False, tax_rate=0),
    )

    # Assert
    assert result == 15 * 1_000_000


def test_geometry_process_shape_unknown_with_print(capsys):
    """process_shape should return 0 for unknown shapes and print when asked."""
    # Arrange
    geometry = _make_geometry()

    # Act
    result = geometry.process_shape(
        "unknown", 1, 2, 3, 4, 5,
        options=ShapeOptions(unit="m", scale=1, precision=2,
                             should_print=True, should_round=True,
                             should_validate=False, tax_rate=0),
    )

    # Assert
    assert result == 0
    assert "Resultado calculado: 0" in capsys.readouterr().out


def test_owner_label():
    """Owner.label() should format the owner's full label."""
    # Arrange
    owner = Owner(
        first_name="Maria",
        last_name="Silva",
        email="maria@example.com",
        phone="88888-8888",
        address="Av. B, 456",
        city="Recife",
        state="PE",
    )

    # Act
    label = owner.label()

    # Assert
    assert label == (
        "Maria Silva <maria@example.com> tel: 88888-8888 - "
        "Av. B, 456, Recife/PE"
    )
