from part_2.PolynomialRing import PolynomialRing


if __name__ == "__main__":
    q = 17
    n = 4

    ring = PolynomialRing(degree=n, modulus=q)

    # a(x) = 2x^2 + 2x + 3
    a = ring.create(coefficients=[3, 2, 2])

    # b(x) = 15x^2 + 1
    b = ring.create(coefficients=[1, 0, 15])

    sum_result = ring.add(first=a, second=b)
    product_result = ring.multiply(first=a, second=b)
    print("a(x) + b(x):", ring.format(sum_result))
    print("a(x) * b(x):", ring.format(product_result))