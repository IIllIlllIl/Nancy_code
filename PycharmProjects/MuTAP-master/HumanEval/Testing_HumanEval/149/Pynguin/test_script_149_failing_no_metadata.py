# Automatically generated by Pynguin.
import script_149 as module_0


def test_case_0():
    try:
        tuple_0 = ()
        list_0 = [tuple_0]
        var_0 = module_0.sorted_list_sum(list_0)
        assert var_0 == [()]
        var_1 = module_0.sorted_list_sum(tuple_0)
    except BaseException:
        pass


def test_case_1():
    try:
        bool_0 = False
        set_0 = {bool_0, bool_0, bool_0, bool_0}
        var_0 = module_0.sorted_list_sum(set_0)
    except BaseException:
        pass


def test_case_2():
    try:
        str_0 = 'wY`jq_^=1CR[c[%y<'
        list_0 = [str_0, str_0, str_0, str_0]
        var_0 = module_0.sorted_list_sum(list_0)
        assert var_0 == []
        tuple_0 = None
        var_1 = module_0.sorted_list_sum(tuple_0)
    except BaseException:
        pass