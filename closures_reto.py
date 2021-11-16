def make_division_by(x):
    def divider(y):
        assert type(y) == int, "Solo números mayores a cero"
        return y / x
    return divider


def run():
    division_by_3 = make_division_by(3)
    print(division_by_3(18))
    division_by_5 = make_division_by(5)
    print(division_by_5(100))
    division_by_18 = make_division_by(18)
    print(division_by_18(54))


if __name__ == "__main__":
    run()