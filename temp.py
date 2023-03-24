import functools
import itertools
import csv


path = r'C:\Users\Kamua\OneDrive\Programação\Python\Projetos\Controle de Estoque\services\bd_ciclo.csv'

with open(path, 'r', encoding='utf-8') as f:
    _reader = csv.reader(f, delimiter=';')
    header = next(_reader)

    reader, reader_copy = itertools.tee(_reader, 2)

    total = functools.reduce(lambda count, _: count + 1, reader_copy, 0)
    print(total)
    count = 0

    for row in reader:
        count += 1
        print(row)

    print(count)