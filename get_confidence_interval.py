# -*- coding: utf-8 -*-

from math import ceil, floor, sqrt
from random import randint


def get_confidence_interval(num_people,
                            num_iter=1000000,
                            percentile=2.576,
                            precision=1e5,
                            num_days=365):
    """
    Compute a 99%-confidence interval for consecutive birthdays probability
    """
    mean = 0.0
    variance = 0.0  # not exactly
    for i in range(1, num_iter + 1):
        x = [randint(1, num_days) for person in range(num_people)]
        x.sort()
        is_consecutive = any(p + 1 == q for (p, q) in zip(x[:-1], x[1:]))
        is_a_loop = (x[0] + num_days - 1 == x[-1])
        is_positive = int(is_consecutive or is_a_loop)
        delta = is_positive - mean
        mean += delta / float(i)
        variance += delta * (is_positive - mean)
    sd = sqrt(variance / float(num_iter - 1))
    lower_bound = mean - percentile * sd / sqrt(num_iter)
    upper_bound = mean + percentile * sd / sqrt(num_iter)
    print("Number of people:"),
    print(num_people),
    print("\tLower bound:"),
    print(floor(lower_bound * precision) / precision),
    print("\tUpper bound:"),
    print(ceil(upper_bound * precision) / precision)
    return lower_bound, upper_bound


def main():
    for num_of_people in range(1, 18):
        (lb, ub) = get_confidence_interval(num_of_people)

    return True


if __name__ == "__main__":
    main()