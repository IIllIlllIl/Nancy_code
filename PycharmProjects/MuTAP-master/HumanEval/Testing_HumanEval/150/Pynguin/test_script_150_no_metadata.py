# Automatically generated by Pynguin.
import script_NDS_150 as module_0


def test_case_2():
    bool_0 = True
    var_0 = module_0.x_or_y(bool_0, bool_0, bool_0)
    assert var_0 is True
    bool_1 = False
    none_type_0 = None
    bool_2 = True
    var_1 = module_0.x_or_y(bool_1, none_type_0, bool_2)


def test_case_3():
    bool_0 = True
    none_type_0 = None
    var_0 = module_0.x_or_y(bool_0, none_type_0, bool_0)
    assert var_0 is True
    bool_1 = False
    var_1 = module_0.x_or_y(bool_0, var_0, bool_0)
    assert var_1 is True
    var_2 = module_0.x_or_y(var_1, var_1, var_1)
    assert var_2 is True
    none_type_1 = None
    var_3 = module_0.x_or_y(var_2, var_2, var_1)
    assert var_3 is True
    var_4 = module_0.x_or_y(var_2, none_type_1, bool_1)
    assert var_4 is False
    int_0 = 300
    var_5 = module_0.x_or_y(int_0, var_2, none_type_1)



def test_case_4():
    bool_0 = True
    none_type_0 = None
    var_0 = module_0.x_or_y(bool_0, none_type_0, bool_0)
    assert var_0 is True
    int_0 = 126
    dict_0 = {int_0: none_type_0, int_0: none_type_0, int_0: var_0, none_type_0: var_0}
    var_1 = module_0.x_or_y(var_0, var_0, dict_0)
    bool_1 = False
    var_2 = module_0.x_or_y(var_0, bool_1, var_0)
    assert var_2 is True
    var_3 = module_0.x_or_y(bool_0, var_0, bool_0)
    assert var_3 is True
    var_4 = module_0.x_or_y(var_3, var_3, var_3)
    assert var_4 is True
    none_type_1 = None
    var_5 = module_0.x_or_y(var_2, var_4, var_3)
    assert var_5 is True
    var_6 = module_0.x_or_y(var_4, none_type_1, bool_1)
    assert var_6 is False
    