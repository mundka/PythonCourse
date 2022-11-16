from calc import Calculator


def test_when_five_is_added_to_six_then_eleven_is_returned():
    device = Calculator()
    assert device.add(5, 6) == 11



def test_whe_twenty_is_added_to_fifty_then_seventy_is_returned():
    object = Calculator()
    assert object.add(20, 50) == 70

def test_when_hundred_is_added_to_fifty_then_result_is_one_fifty():
    calc = Calculator()
    assert calc.add(100, 50) == 150

def test_when_eighty_is_added_to_sevent_then_return_eightyseven():
    new_calc = Calculator()
    assert new_calc.add(80, 7) == 87

def test_when_parameters_are_strings_then_error_is_raised():
    pass

def test_when_only_number_is_given_as_parameter_then_addition_is_successful():
    pass

