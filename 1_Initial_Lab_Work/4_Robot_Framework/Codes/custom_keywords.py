from robot.api.deco import keyword


@keyword("Calculate Total")
def calculate_total(price, quantity):
    return float(price) * int(quantity)


@keyword("Check Positive Number")
def check_positive_number(number):
    return float(number) > 0