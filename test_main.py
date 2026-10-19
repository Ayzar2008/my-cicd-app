from main import add_numbers


def test_add_numbers():
    # пишем 5 вместо 4, чтобы тест упал
    assert add_numbers(2, 2) == 5
