import pytest
from evaluator import Evaluator


def eval_expr(expr: str):
    return Evaluator(expr).evaluate()


def test_complex_1():
    assert eval_expr("5! + (10 $ 20 $ 30) - (2 ^ 4)") == 134.0


def test_complex_2():
    assert eval_expr("123# + (456#) * (10 % 3)") == 21.0


def test_complex_3():
    assert eval_expr("- (10 + 20) * ~ (5 & 2)") == 60.0


def test_complex_4():
    assert eval_expr("(2 ^ 3 ^ 2) @ (100 % 30)") == 37.0


def test_complex_5():
    assert eval_expr("~ (- (5 + 5)) * (2 ^ 3)") == 80.0


def test_complex_6():
    assert eval_expr("12345# + 5! / (10 $ 20)") == 21.0


def test_complex_7():
    assert eval_expr("(100 / 2 / 2) @ (10 * 3 + 5)") == 30.0


def test_complex_8():
    assert eval_expr("((2 + 2)! #) ^ (10 % 8)") == 36.0


def test_complex_9():
    assert eval_expr("- (~ (10)) + (5! @ 60)") == 100.0


def test_complex_10():
    assert eval_expr("((10 $ 20) $ (30 $ 40)) #") == 4.0


def test_complex_11():
    assert eval_expr("(10 + 20 + 30 + 40)# * 2") == 2.0


def test_complex_12():
    assert eval_expr("((5 & 3) $ (10 & 8)) @ 5") == 6.5


def test_complex_13():
    assert eval_expr("100 @ 200 $ 150 & 125") == 125.0


def test_complex_14():
    assert eval_expr("((1 + 1 + 1 + 1 + 1)!) #") == 3.0


def test_complex_15():
    assert eval_expr("10 $ 20 & 15 $ 30 @ 25") == 27.5


def test_complex_16():
    assert eval_expr("((10 @ 20) @ 30) @ 40") == 31.25


def test_complex_17():
    assert eval_expr("3! * 2! * 1! * 0!") == 12.0


def test_complex_18():
    assert eval_expr("(10 $ 10) * (10 & 10) / 10") == 10.0


def test_complex_19():
    with pytest.raises(ValueError):
        eval_expr("(10 + 20 + 30 + 40 + 50) / 0")


def test_complex_20():
    with pytest.raises(ValueError):
        eval_expr("u- (5 + 5 + 5 + 5 + 5) !")