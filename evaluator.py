from enum import Enum
from input_processing import InputProcessing
from operators import operators_priority, binary_functions, unary_prefix_functions, unary_postfix_functions


class EvaluationState(Enum):
    expecting_value = 0
    expecting_operator = 1


class Evaluator:

    def __init__(self, equation: str):
        self.values_stack = []
        self.operators_stack = []
        self.current_evaluation_state = EvaluationState.expecting_value
        self.input_processor = InputProcessing(equation)

    def reset(self, equation: str):
        self.values_stack = []
        self.operators_stack = []
        self.current_evaluation_state = EvaluationState.expecting_value
        self.input_processor.reset(equation)

    def evaluate(self):
        after_tilda: bool = False
        while self.input_processor.has_next():
            current = self.input_processor.get_next()

            if self.current_evaluation_state == EvaluationState.expecting_value:
                if isinstance(current, (float, int)):
                    self.values_stack.append(current)
                    self.current_evaluation_state = EvaluationState.expecting_operator
                elif "u" + current in unary_prefix_functions:
                    if self.operators_stack and current == '~' and self.operators_stack[-1] == 'u-':
                        raise ValueError("Invalid syntax: '~' cant come after '-'")
                    self.operators_stack.append("u" + current)
                    if current == '~':
                        if after_tilda:
                            raise ValueError("Invalid syntax: cant have two or more of '~' for the same number")
                        else:
                            after_tilda = True

                elif current == '(':
                    self.operators_stack.append('(')
                    after_tilda = False
                else:
                    raise ValueError(
                        f"Invalid syntax: at index {self.input_processor.index - 1}: "
                        f"unexpected token '{current}'. "
                        f"Expected a number, '(', or a prefix unary operator.")

            elif self.current_evaluation_state == EvaluationState.expecting_operator:
                if current in binary_functions:
                    if len(self.operators_stack) == 0 or self.operators_stack[-1] == '(':
                        self.operators_stack.append(current)
                    else:
                        while (self.operators_stack and self.operators_stack[-1] != '(' and
                               operators_priority[current] <= operators_priority[self.operators_stack[-1]]):
                            self.apply_top_operator()
                        self.operators_stack.append(current)

                    self.current_evaluation_state = EvaluationState.expecting_value
                elif current in unary_postfix_functions:
                    # print(self.operators_stack)
                    # print(self.values_stack)
                    unary_postfix_before_factorial: bool = False
                    for op in reversed(self.operators_stack):
                        if op == 'u~' or op in binary_functions or op == ('(', ')'):
                            unary_postfix_before_factorial = True
                        if op != 'u-':
                            break

                    while self.operators_stack and self.operators_stack[
                        -1] in unary_prefix_functions and unary_postfix_before_factorial:
                        self.apply_top_operator()

                    result: float = unary_postfix_functions[current](self.values_stack.pop())
                    self.values_stack.append(result)

                elif current == ')':
                    self.clear_stack_until_parenthesis()

                else:
                    raise ValueError(
                        f"Invalid syntax: at index {self.input_processor.index - 1}: "
                        f"unexpected token '{current}'. "
                        f"Expected a binary operator, ')', or a postfix unary operator.")

        if self.current_evaluation_state == EvaluationState.expecting_value and self.input_processor.equation == "":
            raise ValueError("No expression provided")

        if self.current_evaluation_state == EvaluationState.expecting_value:
            raise ValueError("Invalid syntax: expression cannot end with an operator.")

        self.clear_stack()

        if len(self.values_stack) != 1:
            raise ValueError("Invalid syntax: expression could not be fully reduced.")
        return self.values_stack[0]

    def apply_top_operator(self):
        operator: str = self.operators_stack.pop()
        if operator in binary_functions:
            result: float = binary_functions[operator](self.values_stack.pop(), self.values_stack.pop())
        elif operator in unary_prefix_functions:
            result: float = unary_prefix_functions[operator](self.values_stack.pop())
        else:
            raise ValueError("not supposed to be here...")
        self.values_stack.append(result)

    def clear_stack_until_parenthesis(self):
        while self.operators_stack and self.operators_stack[-1] != '(':
            self.apply_top_operator()

        if not self.operators_stack:
            raise ValueError("Invalid syntax: unmatched ')'.")

        self.operators_stack.pop()

    def clear_stack(self):
        while self.operators_stack:
            if self.operators_stack[-1] == '(':
                raise ValueError("Invalid syntax: unmatched '('.")

            self.apply_top_operator()
