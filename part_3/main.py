from part_3.ModulusChain import ModulusChain
from part_3.Rescaler import Rescaler


chain = ModulusChain(1_003, 1_009, 1_013)

rescaler = Rescaler(chain)

value = 3_000_000
scale = 1_000_000
level = chain.initial_level

result = rescaler.rescale(value=value, scale=scale, level=level)

print(f"Valore iniziale: {value}")
print(f"Scala iniziale: {scale}")
print(f"Livello iniziale: {level.index}")
print(f"Modulo iniziale: {chain.modulus_at(level)}")

print()

print(f"Valore dopo il rescaling: {result.value}")
print(f"Scala dopo il rescaling: {result.scale}")
print(f"Livello dopo il rescaling: {result.level.index}")
print(f"Modulo dopo il rescaling: {result.modulus}")
print(f"Fattore eliminato: {result.factor}")