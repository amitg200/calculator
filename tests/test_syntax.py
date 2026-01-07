import pytest
from evaluator import Evaluator


def eval_expr(expr: str):
    return Evaluator(expr).evaluate()


def test_empty_expression():
    with pytest.raises(ValueError):
        eval_expr("")


def test_invalid_character():
    with pytest.raises(ValueError):
        eval_expr("2a+kmd3")


def test_decimal_errors():
    with pytest.raises(ValueError):
        eval_expr(".3+1")
    with pytest.raises(ValueError):
        eval_expr("3.+1")


def test_unmatched_parentheses():
    with pytest.raises(ValueError):
        eval_expr("(2+3")
    with pytest.raises(ValueError):
        eval_expr("2+3)")


def test_two_binary_in_a_row():
    with pytest.raises(ValueError):
        eval_expr("3++4")
    with pytest.raises(ValueError):
        eval_expr("6*/2")


def test_divide_by_zero():
    with pytest.raises(ValueError):
        eval_expr("3/0")


def test_factorial_errors():
    with pytest.raises(ValueError):
        eval_expr("(-3)!")
    with pytest.raises(ValueError):
        eval_expr("2.5!")


def test_sum_digits_errors():
    with pytest.raises(ValueError):
        eval_expr("(-123)#")