import galois
from part_2.examples.functions import encode_vector_to_polynomial, decode_polynomial_to_vector

if __name__ == "__main__":
    q = 23
    N = 4
    GF = galois.GF(q)
    x = galois.Poly.Identity(GF)
    modulus = x ** N + GF(1)
    scale = 10

    m = [1.2, 0.5, 2.1]
    scaled, encoded, message_poly = encode_vector_to_polynomial(values=m, scale=scale, q=q, field=GF, modulus=modulus)
    decoded_coefficients, decoded_message = decode_polynomial_to_vector(poly=message_poly, scale=scale, expected_length=len(m))

    print("Messaggio originale:", m)
    print("Messaggio scalato:", scaled)
    print("Messaggio codificato modulo q:", encoded)
    # 12x^2 + 5x + 21
    print("Messaggio nell'anello:", message_poly)

    print("Coefficienti decodificati:", decoded_coefficients)
    print("Messaggio decodificato:", decoded_message)