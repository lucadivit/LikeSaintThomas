from part_3.exceptions import RescalingError
from part_3.Level import Level
from part_3.ModulusChain import ModulusChain


class RescalingResult:

    def __init__(self, value: int, scale: int, level: Level, modulus: int, factor: int):
        self._value = value
        self._scale = scale
        self._level = level
        self._modulus = modulus
        self._factor = factor

    @property
    def value(self) -> int:
        return self._value

    @property
    def scale(self) -> int:
        return self._scale

    @property
    def level(self) -> Level:
        return self._level

    @property
    def modulus(self) -> int:
        return self._modulus

    @property
    def factor(self) -> int:
        return self._factor


class Rescaler:

    def __init__(self, modulus_chain: ModulusChain):
        self._modulus_chain = modulus_chain

    @property
    def modulus_chain(self) -> ModulusChain:
        return self._modulus_chain

    def rescale(self, value: int, scale: int, level: Level) -> RescalingResult:
        if scale <= 0:
            raise RescalingError("La scala deve essere positiva")

        factor = self._modulus_chain.rescaling_factor_at(level)
        next_modulus = self._modulus_chain.next_modulus_at(level)

        next_value = self._divide_and_round(value, factor)
        next_scale = self._divide_and_round(scale, factor)

        if next_scale <= 0:
            raise RescalingError("La scala risultante deve essere positiva")

        return RescalingResult(value=next_value % next_modulus, scale=next_scale,
                               level=level.next, modulus=next_modulus, factor=factor)

    @staticmethod
    def _divide_and_round(value: int, divisor: int) -> int:
        if divisor <= 0:
            raise RescalingError("Il fattore di rescaling deve essere positivo")

        quotient, remainder = divmod(abs(value), divisor)

        if remainder * 2 >= divisor:
            quotient += 1

        if value < 0:
            return -quotient

        return quotient