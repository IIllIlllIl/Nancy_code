# Automatically generated by Pynguin.
import script_52 as module_0


def test_case_0():
    float_0 = -950.9926
    list_0 = [float_0, float_0, float_0]
    int_0 = -1219
    var_0 = module_0.below_threshold(list_0, int_0)
    assert var_0 is False
    int_1 = 135
    int_2 = 2017
    var_1 = module_0.below_threshold(list_0, int_2)
    assert var_1 is True
    var_2 = module_0.below_threshold(list_0, int_1)
    assert var_2 is True


def test_case_1():
    float_0 = -543.783
    list_0 = [float_0, float_0, float_0]
    int_0 = -782
    int_1 = -2631
    var_0 = module_0.below_threshold(list_0, int_1)
    assert var_0 is False
    var_1 = module_0.below_threshold(list_0, int_0)
    assert var_1 is False