from math import prod

from part_3.exceptions import InvalidLevelError, InvalidModulusChainError
from part_3.Level import Level


class ModulusChain:

    def __init__(self, *factors: int):
        self._validate_factors(factors)

        self._factors = tuple(factors)
        self._moduli = self._build_moduli(self._factors)

    @property
    def factors(self) -> tuple[int, ...]:
        return self._factors

    @property
    def moduli(self) -> tuple[int, ...]:
        return self._moduli

    @property
    def levels_count(self) -> int:
        return len(self._moduli)

    @property
    def rescalings_count(self) -> int:
        return self.levels_count - 1

    @property
    def initial_level(self) -> Level:
        return Level(0)

    @property
    def last_level(self) -> Level:
        return Level(self.levels_count - 1)

    def contains(self, level: Level) -> bool:
        return 0 <= level.index < self.levels_count

    def modulus_at(self, level: Level) -> int:
        self._ensure_level_exists(level)
        return self._moduli[level.index]

    def _ensure_rescaling_is_possible(self, level: Level) -> None:
        self._ensure_level_exists(level)

        if level.index >= self.rescalings_count:
            raise InvalidLevelError(f"Non è possibile effettuare il rescaling dal livello {level.index}")

    def next_modulus_at(self, level: Level) -> int:
        self._ensure_rescaling_is_possible(level)
        return self._moduli[level.next.index]

    def rescaling_factor_at(self, level: Level) -> int:
        current_modulus = self.modulus_at(level)
        next_modulus = self.next_modulus_at(level)

        return current_modulus // next_modulus

    @staticmethod
    def _validate_factors(factors: tuple[int, ...]) -> None:
        if not factors:
            raise InvalidModulusChainError("La catena deve contenere almeno un fattore")

        if any(factor <= 1 for factor in factors):
            raise InvalidModulusChainError("Ogni fattore deve essere maggiore di uno")

    @staticmethod
    def _build_moduli(factors: tuple[int, ...]) -> tuple[int, ...]:
        return tuple(prod(factors[:remaining]) for remaining in range(len(factors), 0, -1))

    def _ensure_level_exists(self, level: Level) -> None:
        if not self.contains(level):
            raise InvalidLevelError(f"Il livello {level.index} non appartiene alla catena dei moduli")

    def __len__(self) -> int:
        return self.levels_count