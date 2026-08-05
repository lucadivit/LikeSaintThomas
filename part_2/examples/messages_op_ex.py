import galois
from part_2.examples.functions import encode_vector_to_polynomial, add_in_ring, multiply_in_ring

if __name__ == "__main__":
    q = 23
    N = 4
    GF = galois.GF(q)
    x = galois.Poly.Identity(GF)
    modulus = x ** N + GF(1)
    scale = 10

    m1 = [1.2, 0.5, 2.1]
    m2 = [0.3, 1.0, 0.4]

    _, _, poly_m1 = encode_vector_to_polynomial(values=m1, scale=scale, q=q, field=GF, modulus=modulus)
    _, _, poly_m2 = encode_vector_to_polynomial(values=m2, scale=scale, q=q, field=GF, modulus=modulus)

    sum_poly = add_in_ring(poly_a=poly_m1, poly_b=poly_m2, modulus=modulus)
    product_poly = multiply_in_ring(poly_a=poly_m1, poly_b=poly_m2, modulus=modulus)

    print("m1 nell'anello:", poly_m1)
    print("m2 nell'anello:", poly_m2)
    print("Somma nell'anello:", sum_poly)
    print("Prodotto nell'anello:", product_poly)