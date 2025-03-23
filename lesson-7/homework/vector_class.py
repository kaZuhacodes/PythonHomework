class Vector:
    def __init__(self, *components):
        self.components = list(components)

    def __repr__(self):
        return f"Vector({', '.join(map(str, self.components))})"

    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimension for addition")
        return Vector(*[a + b for a, b in zip(self.components, other.components)])

    def __sub__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimension for subtraction")
        return Vector(*[a - b for a, b in zip(self.components, other.components)])

    def __mul__(self, other):
        if isinstance(other, Vector):  # Dot product
            if len(self.components) != len(other.components):
                raise ValueError("Vectors must have the same dimension for dot product")
            return sum(a * b for a, b in zip(self.components, other.components))
        elif isinstance(other, (int, float)):  # Scalar multiplication
            return Vector(*[a * other for a in self.components])
        else:
            raise TypeError("Multiplication is only supported for scalars or dot product with another vector")

    def __rmul__(self, other):
        return self * other  # Scalar multiplication (commutative)

    def magnitude(self):
        return sum(a ** 2 for a in self.components) ** 0.5

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector")
        return Vector(*[a / mag for a in self.components])


# Example Usage
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print(v1)          # Output: Vector(1, 2, 3)
print(v1 + v2)     # Output: Vector(5, 7, 9)
print(v2 - v1)     # Output: Vector(3, 3, 3)
print(v1 * v2)     # Output: 32 (dot product)
print(3 * v1)      # Output: Vector(3, 6, 9)
print(v1.magnitude())  # Output: 3.7416573867739413
print(v1.normalize())  # Output: Vector(0.267, 0.534, 0.801)