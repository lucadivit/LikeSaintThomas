import galois
from functions import create_polynomial, reduce_polynomial

if __name__ == "__main__":
    q = 17
    N = 4

    GF = galois.GF(q)
    x = galois.Poly.Identity(GF)
    modulus = x ** N + GF(1)

    # Coefficienti in ordine decrescente di grado: 18x^4 + 4x^3 + 3x^2 + 2x + 1
    coefficients = [18, 4, 3, 2, 1]

    p = create_polynomial(coefficients=coefficients, q=q, field=GF)

    r = reduce_polynomial(poly=p, modulus=modulus)

    print("Campo dei coefficienti:", GF)
    print(f"Anello polinomiale: R_{q} = Z_{q}[x] / (x^{N} + 1)")
    print("Modulo polinomiale:", modulus)
    print("Coefficienti originali:", coefficients)
    print("p(x):", p)
    print(f"p(x) mod (x^{N} + 1):", r)