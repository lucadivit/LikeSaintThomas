class Level:

    def __init__(self, index: int):
        if index < 0:
            raise ValueError("Il livello non può essere negativo")
        self._index = index

    @property
    def index(self) -> int:
        return self._index

    @property
    def next(self) -> "Level":
        return Level(self._index + 1)