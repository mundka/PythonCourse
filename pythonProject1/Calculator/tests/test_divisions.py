from calc import Calculator


def test_when_fifteen_is_divided_by_five_then_ten_is_returned():
    device = Calculator()
    assert device.div(15, 5) == 3


def test_whe_twenty_is_devided_by_2_return_10():
    object = Calculator()
    assert object.div(20, 2) == 10

def test_when_hundred_is_added_to_fifty_then_result_is_one_fifty():
    calc = Calculator()
    assert calc.div(100, 50) == 2

def test_when_eighty_is_added_to_sevent_then_return_eightyseven():
    new_calc = Calculator()
    assert new_calc.div(80, 2) == 40

def test_when_parameters_are_strings_then_error_is_raised():
    calc = Calculator()
    assert calc.add("one", "two") == "three"

def test_when_only_number_is_given_as_parameter_then_addition_is_successful():
    pass

