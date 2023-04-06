def get_zipped(data: dict[str, list]) -> list:
    values = data.values()
    return list(zip(*values))


data = {
    'A': ['1', '2', '3'],
    'B': ['4', '5', '6'],
    'C': ['7', '8', '9'],
}

for value in get_zipped(data):
    print(value)
