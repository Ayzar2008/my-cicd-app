from main import add_numbers

def test_add_numbers():
    # Тест проверяет, что функция работает правильно
    assert add_numbers(2, 2) == 4
    assert add_numbers(-1, 1) == 0
