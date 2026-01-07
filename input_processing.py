from operators import operators_priority


class InputProcessing:

    def __init__(self, equation: str):
        self.index = 0
        self.equation = equation.strip()

    def has_next(self):
        return self.index < len(self.equation)

    def get_next(self):
        is_number: bool = False
        has_decimal: bool = False
        fraction_digit_seen: bool = False

        number: float = 0
        fraction_scale: float = 1

        while self.has_next():
            curr_char = self.equation[self.index]

            if curr_char == ' ':
                self.index += 1
                if is_number:
                    if has_decimal and not fraction_digit_seen:
                        raise ValueError("Decimal point must have digits after it")
                    return number
                continue

            elif curr_char == '.':
                if has_decimal:
                    raise ValueError("There can not be more then one decimal point in the same number")
                if not is_number:
                    raise ValueError("Decimal point must have digits before it")
                self.index += 1
                has_decimal = True
                continue

            elif curr_char.isdigit():
                self.index += 1
                if not has_decimal:
                    is_number = True
                    number *= 10
                    number += int(curr_char)
                else:
                    fraction_digit_seen = True
                    fraction_scale /= 10
                    number += fraction_scale * int(curr_char)

            elif curr_char in operators_priority or curr_char in ('(', ')', '~'):
                if is_number:
                    if has_decimal and not fraction_digit_seen:
                        raise ValueError("Decimal point must have digits after it")
                    return number
                self.index += 1
                return curr_char

            else:
                raise ValueError(
                    f"The equation you entered contains undefine character '{curr_char}' at index {self.index}")

        if has_decimal and not fraction_digit_seen:
            raise ValueError("Decimal point must have digits after it")

        return number
