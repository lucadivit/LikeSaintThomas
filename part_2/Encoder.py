from part_2.PolynomialRing import PolynomialRing

class Encoder:

    def __init__(self, scale: int, polynomial_ring: PolynomialRing):
        if scale <= 0:
            raise ValueError("La scala deve essere positiva")

        self._scale = scale
        self._polynomial_ring = polynomial_ring

    @property
    def scale(self) -> int:
        return self._scale

    @property
    def polynomial_ring(self) -> PolynomialRing:
        return self._polynomial_ring

    def encode_value(self, value: float) -> int:
        return round(value * self._scale)

    def decode_value(self, value: int) -> float:
        return value / self._scale

    def encode(self, values: list[float]) -> list[int]:
        coefficients = [self.encode_value(value) for value in values]
        coefficients.reverse()
        return self._polynomial_ring.create(coefficients)

    def decode(self, polynomial: list[int], expected_length: int) -> list[float]:
        coefficients = polynomial[:expected_length]
        coefficients.reverse()
        return [self.decode_value(coefficient) for coefficient in coefficients]