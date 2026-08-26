from part_2.Encoder import Encoder
from part_2.PolynomialRing import PolynomialRing


q = 23
n = 4
scale = 10

first_message = [1.2, 0.5, 2.1]
second_message = [0.3, 1.0, 0.4]

ring = PolynomialRing(degree=n, modulus=q)
encoder = Encoder(scale=scale, polynomial_ring=ring)

first_polynomial = encoder.encode(values=first_message)
second_polynomial = encoder.encode(values=second_message)

sum_polynomial = ring.add(
    first=first_polynomial,
    second=second_polynomial,
)

product_polynomial = ring.multiply(
    first=first_polynomial,
    second=second_polynomial,
)

decoded_first_message = encoder.decode(
    polynomial=first_polynomial,
    expected_length=len(first_message),
)

decoded_second_message = encoder.decode(
    polynomial=second_polynomial,
    expected_length=len(second_message),
)

decoded_sum = encoder.decode(
    polynomial=sum_polynomial,
    expected_length=len(first_message),
)

print(f"Anello: R_{q} = Z_{q}[x] / (x^{n} + 1)")
print(f"Scala: {scale}")
print()

print("Primo messaggio:", first_message)
print("Primo polinomio:", ring.format(first_polynomial))
print("Primo messaggio decodificato:", decoded_first_message)
print()

print("Secondo messaggio:", second_message)
print("Secondo polinomio:", ring.format(second_polynomial))
print("Secondo messaggio decodificato:", decoded_second_message)
print()

print("Somma nell'anello:", ring.format(sum_polynomial))
print("Somma decodificata:", decoded_sum)
print()

print("Prodotto nell'anello:", ring.format(product_polynomial))
print("Scala del prodotto:", scale**2)