# Source d'inspiration :
# http://stackoverflow.com/questions/3025162/statistics-combinations-in-python/3025547#3025547


def choose(n, k):
    """
    A fast way to calculate binomial coefficients by Andrew Dalke (contrib).
    """
    if 0 <= k <= n:
        ntok = 1
        ktok = 1
        for t in range(1, min(k, n - k) + 1):
            ntok *= n
            ktok *= t
            n -= 1
        return ntok // ktok
    else:
        return 0


def get_my_guess(num_people, num_days=365):
    """
    Compute my initial guess of the consecutive birthdays probability
    """
    left_result = 1 - (num_people - 1) / float(2 * num_days + num_people - 1)
    right_result = 1
    for i in range(num_people):
        right_result *= (num_days - 2 * i) / float(num_days)
    guess = left_result * (1 - right_result)
    print(f"Number of people: {num_people}\tMy guess: {guess:2.5%}")
    return guess


def get_correct_solution(num_people, num_days=365, limit_overflow=1e42):
    """
    Compute the consecutive birthdays probability
    """
    result = 0
    for k in range(1, num_people + 1):
        my_product = 1 / float(k * pow(num_days, num_people - k))
        for i in range(1, k):
            my_product *= (num_days - (k + i)) / float(num_days * i)
        my_sum = 0
        for j in range(0, k + 1):
            my_sum += pow(-1, j) * choose(k, j) * pow(k - j, num_people)
        result += my_product * my_sum
        if my_sum > limit_overflow:
            raise OverflowError
    proba = 1 - result
    print(f"Number of people: {num_people}\tSolution: {proba:2.5%}")
    return proba


def main():
    for num_of_people in range(1, 34):
        try:
            _ = get_correct_solution(num_of_people)
            _ = get_my_guess(num_of_people)
        except OverflowError:
            break

    return True


if __name__ == "__main__":
    main()
