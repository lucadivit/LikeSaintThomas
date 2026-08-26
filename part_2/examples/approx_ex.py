from part_2.Encoder import Encoder
from part_2.PolynomialRing import PolynomialRing


if __name__ == "__main__":
    q = 17
    n = 4
    scale = 10

    ring = PolynomialRing(degree=n, modulus=q)

    encoder = Encoder(scale=scale, polynomial_ring=ring)

    for value in [1.2, 1.83]:
        scaled_value = encoder.encode_value(value)
        encoded_value = scaled_value % q
        decoded_value = encoder.decode_value(encoded_value)

        print("Messaggio originale:", value)
        print("Messaggio scalato:", scaled_value)
        print("Messaggio codificato modulo q:", encoded_value)
        print("Messaggio decodificato:", decoded_value)
        print()