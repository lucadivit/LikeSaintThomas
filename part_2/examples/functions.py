import galois


def create_polynomial(coefficients, q, field):
    """
    Costruisce un polinomio riducendo prima i coefficienti modulo q.

    I coefficienti devono essere forniti in ordine decrescente di grado.
    """
    reduced_coefficients = [coefficient % q for coefficient in coefficients]

    return galois.Poly(reduced_coefficients, field=field)


def reduce_polynomial(poly, modulus):
    """
    Riduce un polinomio modulo il polinomio x^N + 1.
    """
    return poly % modulus


def add_in_ring(poly_a, poly_b, modulus):
    """
    Somma due polinomi e riduce il risultato nell'anello.
    """
    return reduce_polynomial(poly=poly_a + poly_b, modulus=modulus)


def multiply_in_ring(poly_a, poly_b, modulus):
    """
    Moltiplica due polinomi e riduce il risultato nell'anello.
    """
    return reduce_polynomial(poly=poly_a * poly_b, modulus=modulus)

def encode_real(value, scale, q):
    """
    Codifica un numero reale come intero scalato
    e lo riduce modulo q.
    """
    scaled_value = round(value * scale)
    encoded_value = scaled_value % q

    return scaled_value, encoded_value


def decode_real(encoded_value, scale):
    """
    Decodifica un intero scalato riportandolo
    a numero reale approssimato.
    """
    return encoded_value / scale

def encode_vector_to_polynomial(values, scale, q, field, modulus):
    """
    Codifica un vettore di numeri reali come polinomio.

    Ogni valore viene codificato come intero scalato modulo q
    e poi usato come coefficiente del polinomio.

    I coefficienti sono in ordine decrescente di grado,
    come richiesto da galois.Poly.
    """
    scaled_values = []
    encoded_values = []

    for value in values:
        scaled_value, encoded_value = encode_real(value=value, scale=scale, q=q)

        scaled_values.append(scaled_value)
        encoded_values.append(encoded_value)

    message_poly = reduce_polynomial(poly=create_polynomial(coefficients=encoded_values, q=q, field=field), modulus=modulus)

    return scaled_values, encoded_values, message_poly

def decode_polynomial_to_vector(poly, scale, expected_length):
    """
    Decodifica un polinomio in un vettore di numeri reali approssimati.

    I coefficienti vengono letti in ordine decrescente di grado,
    coerentemente con galois.Poly.
    """
    coefficients = [int(coefficient) for coefficient in poly.coeffs]

    if len(coefficients) < expected_length:
        padding = [0] * (expected_length - len(coefficients))
        coefficients = padding + coefficients

    coefficients = coefficients[-expected_length:]

    decoded_values = [decode_real(encoded_value=coefficient, scale=scale) for coefficient in coefficients]

    return coefficients, decoded_values