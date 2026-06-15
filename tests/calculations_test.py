# System Modules
import sys
import os

# Installed Modules
import pytest

# Project Modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from calculations import (   # noqa: E402
    area_of_circle,
    get_nth_fibonacci,
    area_of_circle_meters,
    area_of_circle_cm,
    area_of_circle_mm,
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
    assert abs(result - 3.14159) < 1e-5


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


def test_area_of_circle_meters():
    """Test area in square meters."""
    # Arrange
    radius = 2

    # Act
    result = area_of_circle_meters(radius)

    # Assert
    assert abs(result - (3.14159 * 4)) < 1e-5


def test_area_of_circle_cm():
    """Test area converted to square centimeters."""
    # Arrange
    radius = 2

    # Act
    result = area_of_circle_cm(radius)

    # Assert
    assert abs(result - (3.14159 * 4 * 10000)) < 1e-2


def test_area_of_circle_mm():
    """Test area converted to square millimeters."""
    # Arrange
    radius = 2

    # Act
    result = area_of_circle_mm(radius)

    # Assert
    assert abs(result - (3.14159 * 4 * 1000000)) < 1


def test_area_of_circle_meters_negative():
    """Test that a negative radius raises an error."""
    # Arrange
    radius = -1

    # Act & Assert
    with pytest.raises(ValueError, match="Radius cannot be negative"):
        area_of_circle_meters(radius)


def test_area_of_circle_cm_negative():
    """Test that a negative radius raises an error in cm."""
    # Arrange
    radius = -1

    # Act & Assert
    with pytest.raises(ValueError, match="Radius cannot be negative"):
        area_of_circle_cm(radius)


def test_area_of_circle_mm_negative():
    """Test that a negative radius raises an error in mm."""
    # Arrange
    radius = -1

    # Act & Assert
    with pytest.raises(ValueError, match="Radius cannot be negative"):
        area_of_circle_mm(radius)


def _make_geometry():
    """Helper that builds a Geometry instance for the tests."""
    return Geometry(
        name="figuras",
        owner="João",
        owner_email="joao@example.com",
        owner_phone="99999-9999",
        owner_address="Rua A, 123",
    )


def test_geometry_process_shape_rectangle():
    """process_shape should compute a simple rectangle area."""
    # Arrange
    geometry = _make_geometry()

    # Act
    result = geometry.process_shape(
        "rectangle", 2, 3, 0, 0, 0,
        unit="m", scale=1, precision=2,
        should_print=False, should_round=True,
        should_validate=True, tax_rate=0,
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
        unit="cm", scale=1, precision=4,
        should_print=False, should_round=True,
        should_validate=True, tax_rate=10,
    )

    # Assert
    expected = round(3.14159 * 10000 * 1.10, 4)
    assert result == expected


def test_geometry_process_shape_validation_error():
    """process_shape should reject negative dimensions when validating."""
    # Arrange
    geometry = _make_geometry()

    # Act & Assert
    with pytest.raises(ValueError, match="No negatives allowed"):
        geometry.process_shape(
            "rectangle", -1, 3, 0, 0, 0,
            unit="m", scale=1, precision=2,
            should_print=False, should_round=False,
            should_validate=True, tax_rate=0,
        )


def test_geometry_process_shape_triangle():
    """process_shape should compute a triangle area."""
    # Arrange
    geometry = _make_geometry()

    # Act
    result = geometry.process_shape(
        "triangle", 4, 3, 0, 0, 0,
        unit="m", scale=1, precision=2,
        should_print=False, should_round=True,
        should_validate=False, tax_rate=0,
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
        unit="m", scale=1, precision=2,
        should_print=False, should_round=True,
        should_validate=False, tax_rate=0,
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
        unit="m", scale=1, precision=2,
        should_print=False, should_round=True,
        should_validate=False, tax_rate=0,
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
        unit="mm", scale=1, precision=2,
        should_print=False, should_round=True,
        should_validate=False, tax_rate=0,
    )

    # Assert
    assert result == 15 * 1000000


def test_geometry_process_shape_unknown_with_print(capsys):
    """process_shape should return 0 for unknown shapes and print when asked."""
    # Arrange
    geometry = _make_geometry()

    # Act
    result = geometry.process_shape(
        "unknown", 1, 2, 3, 4, 5,
        unit="m", scale=1, precision=2,
        should_print=True, should_round=True,
        should_validate=False, tax_rate=0,
    )

    # Assert
    assert result == 0
    assert "Resultado calculado: 0" in capsys.readouterr().out


def test_geometry_build_owner_label():
    """build_owner_label should format an owner's full label."""
    # Arrange
    geometry = _make_geometry()
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
    label = geometry.build_owner_label(owner)

    # Assert
    assert label == (
        "Maria Silva <maria@example.com> tel: 88888-8888 - "
        "Av. B, 456, Recife/PE"
    )