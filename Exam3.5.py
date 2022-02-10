number = 7438


def get_sum(summary: int):
    f = 0
    for i in str(summary):
        f += int(i)
    print(f)


get_sum(number)