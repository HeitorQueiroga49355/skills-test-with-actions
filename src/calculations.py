# System Modules
import math
from dataclasses import dataclass, field

# Installed Modules
# - None

_UNIT_MULTIPLIERS = {"m": 1, "cm": 10_000, "mm": 1_000_000}


def area_of_circle(radius):
    """Calculate the area of a circle given its radius."""
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2


def area_of_circle_in_unit(radius, unit="m"):
    """Calculate circle area converted to the given unit (m, cm, or mm)."""
    return area_of_circle(radius) * _UNIT_MULTIPLIERS.get(unit, 1)


def get_nth_fibonacci(n):
    """Calculate the nth Fibonacci number."""
    if n < 0:
        raise ValueError("n cannot be negative")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b


@dataclass
class ShapeOptions:
    unit: str = "m"
    scale: float = 1
    precision: int = 2
    should_print: bool = False
    should_round: bool = True
    should_validate: bool = True
    tax_rate: float = 0


class Owner:
    def __init__(self, first_name, last_name, email, phone, address, city, state):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address
        self.city = city
        self.state = state

    def label(self):
        return (
            f"{self.first_name} {self.last_name} <{self.email}>"
            f" tel: {self.phone} - {self.address}, {self.city}/{self.state}"
        )


class Geometry:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.shapes = []

    def _compute_shape(self, shape_type, a, b, c, d, e):
        if shape_type == "circle":
            return math.pi * a * a
        if shape_type == "rectangle":
            return a * b
        if shape_type == "triangle":
            return (a * b) / 2
        if shape_type == "trapezoid":
            return ((a + b) / 2) * c
        if shape_type == "box":
            return a * b * c
        if shape_type == "weird":
            return a + b + c + d + e
        return 0

    def process_shape(self, shape_type, a, b, c, d, e, options=None):
        if options is None:
            options = ShapeOptions()

        if options.should_validate and any(v < 0 for v in (a, b, c, d, e)):
            raise ValueError("No negatives allowed")

        result = self._compute_shape(shape_type, a, b, c, d, e)
        result *= _UNIT_MULTIPLIERS.get(options.unit, 1)
        result *= options.scale
        result += result * options.tax_rate / 100

        if options.should_round:
            result = round(result, options.precision)
        if options.should_print:
            print("Resultado calculado: " + str(result))

        self.shapes.append(result)
        return result
