def find_height(cubes):
    # Code goes here

    layers = 0

    while (layers * (layers + 1) * (layers + 2)) / 6 <= cubes:
        layers += 1

    return layers -1