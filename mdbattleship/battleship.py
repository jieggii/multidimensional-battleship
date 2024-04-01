class Battleship:
    _order: int
    _vectors: list[tuple[int, ...]]

    def __init__(self, vectors: list[tuple[int, ...]]):
        if len(vectors) == 0:
            raise ValueError("empty vectors")

        # verify order consistency across vectors:
        order = len(vectors[0])
        for i, vector in enumerate(vectors[1:]):
            current_order = len(vector)
            if current_order != order:
                raise ValueError(
                    f"non-consistent vector orders (vector {i + 1} has order = {current_order}, "
                    f"but the order of the vector 0 is {order})",
                )
        self._order = order
        self._vectors = vectors

    @property
    def order(self) -> int | None:
        return self._order

    @property
    def vectors(self) -> list[tuple[int, ...]]:
        return self._vectors
