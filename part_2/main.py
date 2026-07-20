import galois


def create_polynomial(coefficients, q, field):
    """
    Costruisce un polinomio riducendo prima i coefficienti modulo q.

    I coefficienti devono essere forniti in ordine decrescente di grado.
    """
    reduced_coefficients = [
        coefficient % q
        for coefficient in coefficients
    ]

    return galois.Poly(reduced_coefficients, field=field)


def reduce_polynomial(poly, modulus):
    """
    Riduce un polinomio modulo il polinomio x^N + 1.
    """
    return poly % modulus

q = 17
N = 4

GF = galois.GF(q)

x = galois.Poly.Identity(GF)
modulus = x**N + GF(1)

# Coefficienti in ordine decrescente di grado: 18x^4 + 4x^3 + 3x^2 + 2x + 1
coefficients = [18, 4, 3, 2, 1]

p = create_polynomial(coefficients=coefficients, q=q, field=GF)

r = reduce_polynomial(poly=p, modulus=modulus)

print("Campo dei coefficienti:", GF)
print("Modulo polinomiale:", modulus)
print("Coefficienti originali:", coefficients)
print("p(x):", p)
print("p(x) mod (x^N + 1):", r)