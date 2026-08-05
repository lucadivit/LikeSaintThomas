import galois


class PolynomialRing:

    def __init__(self, degree: int, modulus: int):
        if degree <= 0:
            raise ValueError("Il grado dell'anello deve essere positivo")

        if degree & (degree - 1) != 0:
            raise ValueError("Il grado dell'anello deve essere una potenza di due")

        if modulus <= 1:
            raise ValueError("Il modulo deve essere maggiore di uno")

        self._degree = degree
        self._modulus = modulus
        self._field = galois.GF(modulus)

        x = galois.Poly.Identity(self._field)
        self._polynomial_modulus = (
            x ** self._degree + self._field(1)
        )

    @property
    def degree(self) -> int:
        return self._degree

    @property
    def modulus(self) -> int:
        return self._modulus

    def create(self, coefficients: list[int]) -> galois.Poly:
        reduced_coefficients = [coefficient % self._modulus for coefficient in coefficients]

        polynomial = galois.Poly(reduced_coefficients, field=self._field)

        return self.reduce(polynomial)

    def reduce(self, polynomial: galois.Poly) -> galois.Poly:
        return polynomial % self._polynomial_modulus

    def add(self, first: galois.Poly, second: galois.Poly) -> galois.Poly:
        return self.reduce(first + second)

    def multiply(self, first: galois.Poly, second: galois.Poly) -> galois.Poly:
        return self.reduce(first * second)