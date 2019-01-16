# -*- coding: utf-8 -*-

from math import sqrt
from random import randint


def get_confidence_interval(num_people,
                            num_iter=1000000,
                            percentile=2.576,
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
    print(
        "Number of people: {}\tLower bound: {:2.5%}\tUpper bound: {:2.5%}".format(num_people, lower_bound, upper_bound))
    return lower_bound, upper_bound


def main():
    for num_of_people in range(1, 18):
        _, _ = get_confidence_interval(num_of_people)

    return True


if __name__ == "__main__":
    main()
