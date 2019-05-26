# chunk file


def read_file():
    with open('./data/textfile.txt') as f:
        print(f)


def read_lines():
    with open('./data/textfile.txt') as f:
        for line in f:
            print(line)


def chunk_file():
    from functools import partial
    blocks = []
    with open('./data/textfile.txt') as f:
        for block in iter(partial(f.read, 32), ''):
            blocks.append(block.replace('\n', '##'))
    print(blocks)


def hash_file():
    from functools import partial
    h = {}
    with open('./data/textfile.txt') as f:
        i = 0
        for line in f:
            i += 1
            x, y = line.rstrip('\n').split(",")
            h[i] = [int(x), int(y)]
    print(h)


def read_csv_file():
    import csv
    with open('../data/textfile.txt') as f:
        csv_file = csv.reader(f, delimiter=',')
        birth_years = []
        death_years = []
        for line in csv_file:
            birth = line[0]
            death = line[1]

            birth_years.append(birth)
            death_years.append(death)

        print(birth_years)
        print(death_years)


def read_json_file():
    import json
    with open('../data/textfile.json', 'r') as f:
        json_file = f.read()
    json_dictionary = json.loads(json_file)
    print(json_dictionary)

