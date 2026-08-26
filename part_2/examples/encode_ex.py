from part_2.Encoder import Encoder
from part_2.PolynomialRing import PolynomialRing


if __name__ == "__main__":
    q = 23
    n = 4
    scale = 10

    ring = PolynomialRing(degree=n, modulus=q)
    encoder = Encoder(scale=scale, polynomial_ring=ring)

    message = [1.2, 0.5, 2.1]
    scaled_values = [encoder.encode_value(value) for value in message]
    message_polynomial = encoder.encode(values=message)
    decoded_message = encoder.decode(polynomial=message_polynomial, expected_length=len(message))

    print("Messaggio originale:", message)
    print("Messaggio scalato:", scaled_values)
    print("Messaggio nell'anello:", ring.format(message_polynomial))
    print("Messaggio decodificato:", decoded_message)