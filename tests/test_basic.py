import pytest
from evaluator import Evaluator


def eval_expr(expr: str):
    return Evaluator(expr).evaluate()


def test_basic_add_sub():
    assert eval_expr("1+2") == 3
    assert eval_expr("10-7") == 3
    assert eval_expr("7-10") == -3


def test_mul_div_precedence():
    assert eval_expr("2+3*4") == 14
    assert eval_expr("(2+3)*4") == 20
    assert eval_expr("20/5+1") == 5


def test_power_precedence():
    assert eval_expr("2^3") == 8
    assert eval_expr("2^3*2") == 16
    assert eval_expr("2*(3^2)") == 18


def test_modulo():
    assert eval_expr("20%6") == 2
    assert eval_expr("5+20%6") == 7


def test_max_min_avg():
    assert eval_expr("7$2") == 7
    assert eval_expr("7&2") == 2
    assert eval_expr("8@2") == 5


def test_unary_minus_basic():
    assert eval_expr("-3") == -3
    assert eval_expr("--3") == 3
    assert eval_expr("2--3") == 5
    assert eval_expr("2+-3") == -1


def test_tilda_invert():
    assert eval_expr("~3") == -3
    assert eval_expr("~(7)") == -7
    assert eval_expr("~(-7)") == 7
    assert eval_expr("3+~3") == 0


def test_factorial_simple():
    assert eval_expr("0!") == 1
    assert eval_expr("1!") == 1
    assert eval_expr("3!") == 6
    assert eval_expr("5!") == 120


def test_factorial_with_expression():
    assert eval_expr("(2+3)!") == 120
    assert eval_expr("2*(3!)") == 12


def test_sum_digits_operator():
    assert eval_expr("123#") == 6
    assert eval_expr("2.3#") == 5
    assert eval_expr("99##") == 9


def test_spaces_are_ok():
    assert eval_expr("  8 - 8 + (  90 * 7  ) ") == (8 - 8 + (90 * 7))


def test_float_precision():
    assert eval_expr("1.2+3.4") == pytest.approx(4.6)
    assert eval_expr("10/4") == pytest.approx(2.5)


def test_single_number():
    evaluator = Evaluator("7")
    assert evaluator.evaluate() == 7


def test_simple_division():
    evaluator = Evaluator("20/4")
    assert evaluator.evaluate() == 5


def test_simple_subtraction():
    evaluator = Evaluator("10-4")
    assert evaluator.evaluate() == 6
