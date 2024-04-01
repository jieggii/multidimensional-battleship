def generate_delta_vectors(order: int):
    def generate_delta_recursive(delta, depth):
        if depth == order:
            return [tuple(delta)]

        delta_vectors = []
        for offset in (-1, 0, 1):
            delta[depth] = offset
            sub_deltas = generate_delta_recursive(delta, depth + 1)
            delta_vectors.extend(sub_deltas)

        return delta_vectors

    deltas = generate_delta_recursive([0] * order, 0)
    deltas.remove((0,) * order)  # Remove the zero vector
    return deltas


def init_multidimensional_list(shape: tuple[int, ...], value: int) -> list:
    if len(shape) == 1:
        return [value] * shape[0]
    else:
        return [init_multidimensional_list(shape[1:], value) for _ in range(shape[0])]


def print_multidimensional_list(x: list):
    if isinstance(x, list) and isinstance(x[0], list):
        for subfield in x:
            print_multidimensional_list(subfield)
    else:
        for item in x:
            print(item, end=" ")
    print()
