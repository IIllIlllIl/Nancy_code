# Automatically generated by Pynguin.
import script_37 as module_0


def test_case_0():
    float_0 = 890.6
    list_0 = [float_0, float_0, float_0, float_0]
    var_0 = module_0.sort_even(list_0)
    assert len(var_0) == 4
    assert module_0.METADATA == {}


def test_case_1():
    str_0 = '_*s^F\x0b\x0c7t4EPy8r+|Er@'
    list_0 = [str_0]
    var_0 = module_0.sort_even(list_0)
    assert var_0 == ['_*s^F\x0b\x0c7t4EPy8r+|Er@']
    assert module_0.METADATA == {}
    list_1 = []
    var_1 = module_0.sort_even(list_1)
    assert var_1 == []
    var_2 = module_0.sort_even(list_1)
    assert var_2 == []
    var_3 = module_0.sort_even(list_1)
    assert var_3 == []
