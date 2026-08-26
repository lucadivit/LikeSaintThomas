from part_2.PolynomialRing import PolynomialRing


if __name__ == "__main__":
    q = 17
    n = 4

    ring = PolynomialRing(degree=n, modulus=q)

    # p(x) = 18x^4 + 4x^3 + 3x^2 + 2x + 1
    coefficients = [1, 2, 3, 4, 18]
    polynomial = ring.create(coefficients=coefficients)

    print(f"Anello polinomiale: R_{q} = Z_{q}[x] / (x^{n} + 1)")
    print("Coefficienti originali:", coefficients)
    print(f"p(x) mod (x^{n} + 1):", ring.format(polynomial))