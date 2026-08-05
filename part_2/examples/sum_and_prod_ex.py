import galois
from part_2.examples.functions import create_polynomial, reduce_polynomial, add_in_ring, multiply_in_ring

if __name__ == "__main__":
    q = 17
    N = 4

    GF = galois.GF(q)
    x = galois.Poly.Identity(GF)
    modulus = x ** N + GF(1)

    # a(x) = 2x^2 + 2x + 3
    a = reduce_polynomial(poly=create_polynomial(coefficients=[2, 2, 3], q=q, field=GF), modulus=modulus)

    # b(x) = 15x^2 + 1
    b = reduce_polynomial(poly=create_polynomial(coefficients=[15, 0, 1], q=q, field=GF), modulus=modulus)

    sum_result = add_in_ring(poly_a=a, poly_b=b, modulus=modulus)
    product_result = multiply_in_ring(poly_a=a, poly_b=b, modulus=modulus)
    print(f"a(x) + b(x): {sum_result}")
    print(f"a(x) * b(x): {product_result}")