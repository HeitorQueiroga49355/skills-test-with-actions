# System Modules
import math

# Installed Modules
# - None


def area_of_circle(radius):
    """Calculate the area of a circle given its radius."""
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2


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


# --- Duplicated Code: as três funções abaixo repetem a mesma lógica ---
def area_of_circle_meters(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return 3.14159 * radius * radius


def area_of_circle_cm(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return 3.14159 * radius * radius * 10000


def area_of_circle_mm(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return 3.14159 * radius * radius * 1000000


class Geometry:
    """Large Class: faz cálculos, formatação, relatório e e-mail ao mesmo tempo."""

    def __init__(self, name, owner, owner_email, owner_phone, owner_address):
        self.name = name
        # Data Clumps: dono sempre representado por estes 4 campos juntos
        self.owner = owner
        self.owner_email = owner_email
        self.owner_phone = owner_phone
        self.owner_address = owner_address
        self.shapes = []

    # Long Method + Long Parameter List + Magic Numbers
    def process_shape(self, shape_type, a, b, c, d, e, unit, scale, precision,
                      should_print, should_round, should_validate, tax_rate):
        result = 0
        if should_validate:
            if a < 0 or b < 0 or c < 0 or d < 0 or e < 0:
                raise ValueError("No negatives allowed")
        if shape_type == "circle":
            result = 3.14159 * a * a
        elif shape_type == "rectangle":
            result = a * b
        elif shape_type == "triangle":
            result = (a * b) / 2
        elif shape_type == "trapezoid":
            result = ((a + b) / 2) * c
        elif shape_type == "box":
            result = a * b * c
        elif shape_type == "weird":
            result = a + b + c + d + e
        else:
            result = 0
        if unit == "cm":
            result = result * 10000
        elif unit == "mm":
            result = result * 1000000
        result = result * scale
        result = result + (result * tax_rate / 100)
        if should_round:
            result = round(result, precision)
        if should_print:
            print("Resultado calculado: " + str(result))
        self.shapes.append(result)
        return result

    # Feature Envy: mexe quase só nos dados de Owner, não nos próprios
    def build_owner_label(self, owner):
        return (owner.first_name + " " + owner.last_name + " <" +
                owner.email + "> tel: " + owner.phone + " - " +
                owner.address + ", " + owner.city + "/" + owner.state)


class Owner:
    def __init__(self, first_name, last_name, email, phone, address, city, state):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.address = address
        self.city = city
        self.state = state
