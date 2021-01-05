import itertools
from functools import reduce


def get_clean_data(file: str):
    return [int(entry.strip()) for entry in open(file, "r")]


def get_values_that_sum_2020(data, num_values):
    for values in itertools.combinations(data, num_values):
        if sum(values) == 2020:
            return values

    raise Exception("No values in data sum to 2020")


if __name__ == '__main__':
    clean_data = get_clean_data("data.txt")
    values = get_values_that_sum_2020(clean_data, 3)
    print(reduce(lambda x, y: x * y, values))
