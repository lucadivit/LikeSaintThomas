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

    @property
    def degree(self) -> int:
        return self._degree

    @property
    def modulus(self) -> int:
        return self._modulus

    def create(self, coefficients: list[int]) -> list[int]:
        reduced_coefficients = [coefficient % self._modulus for coefficient in coefficients]

        if len(reduced_coefficients) < self._degree:
            reduced_coefficients += [0] * (self._degree - len(reduced_coefficients))

        return self.reduce(reduced_coefficients)

    def reduce(self, coefficients: list[int]) -> list[int]:
        result = coefficients[:]

        while len(result) > self._degree:
            coefficient = result.pop()
            target_index = len(result) - self._degree
            result[target_index] -= coefficient

        return [coefficient % self._modulus for coefficient in result]

    def add(self, first: list[int], second: list[int]) -> list[int]:
        return [(first[index] + second[index]) % self._modulus for index in range(self._degree)]

    def multiply(self, first: list[int], second: list[int]) -> list[int]:
        product = [0] * (2 * self._degree - 1)

        for first_index, first_coefficient in enumerate(first):
            for second_index, second_coefficient in enumerate(second):
                product[first_index + second_index] += (first_coefficient * second_coefficient)

        return self.reduce(product)

    def format(self, polynomial: list[int]) -> str:
        terms = []

        for exponent in range(len(polynomial) - 1, -1, -1):
            coefficient = polynomial[exponent]

            if coefficient == 0:
                continue

            if exponent == 0:
                term = str(coefficient)

            elif exponent == 1:
                if coefficient == 1:
                    term = "x"
                else:
                    term = f"{coefficient}x"

            else:
                if coefficient == 1:
                    term = f"x^{exponent}"
                else:
                    term = f"{coefficient}x^{exponent}"

            terms.append(term)

        if not terms:
            return "0"

        return " + ".join(terms)