from part_2.Encoder import Encoder
from part_2.PolynomialRing import PolynomialRing


if __name__ == "__main__":
    q = 23
    n = 4
    scale = 10

    ring = PolynomialRing(degree=n, modulus=q)
    encoder = Encoder(scale=scale, polynomial_ring=ring)

    m1 = [1.2, 0.5, 2.1]
    m2 = [0.3, 1.0, 0.4]
    poly_m1 = encoder.encode(values=m1)
    poly_m2 = encoder.encode(values=m2)

    sum_polynomial = ring.add(first=poly_m1, second=poly_m2)
    product_polynomial = ring.multiply(first=poly_m1, second=poly_m2)

    print("m1 nell'anello:", ring.format(poly_m1))
    print("m2 nell'anello:", ring.format(poly_m2))
    print("Somma nell'anello:", ring.format(sum_polynomial))
    print("Prodotto nell'anello:", ring.format(product_polynomial))