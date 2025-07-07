from ex24 import secret_formula

def test_secret_formula():
    assert secret_formula(10_000) == (5_000_000, 5000, 50)
