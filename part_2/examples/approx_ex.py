from part_2.examples.functions import encode_real, decode_real

if __name__ == "__main__":
    q = 17
    scale = 10

    for m in [1.2, 1.83]:
        scaled, encoded = encode_real(value=m, scale=scale, q=q)
        decoded = decode_real(encoded_value=encoded, scale=scale)

        print("Messaggio originale:", m)
        print("Messaggio scalato:", scaled)
        print("Messaggio codificato modulo q:", encoded)
        print("Messaggio decodificato:", decoded)