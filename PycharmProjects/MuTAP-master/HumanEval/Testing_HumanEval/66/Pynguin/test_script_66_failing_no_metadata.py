# Automatically generated by Pynguin.
import script_66 as module_0


def test_case_0():
    try:
        bool_0 = False
        set_0 = {bool_0, bool_0, bool_0, bool_0}
        var_0 = module_0.digitSum(set_0)
    except BaseException:
        pass


def test_case_1():
    try:
        set_0 = set()
        bytes_0 = b'\x9a\xb7\xd1\x1e\xa9:j\xcfT\xb8\x1d'
        tuple_0 = bytes_0,
        var_0 = module_0.digitSum(tuple_0)
        assert var_0 == 0
        tuple_1 = set_0, set_0
        var_1 = module_0.digitSum(tuple_1)
    except BaseException:
        pass


def test_case_2():
    try:
        str_0 = '~3`SL6`d[-9Z'
        var_0 = module_0.digitSum(str_0)
        assert var_0 == 249
        bool_0 = False
        set_0 = {bool_0, bool_0, bool_0, bool_0}
        var_1 = module_0.digitSum(set_0)
    except BaseException:
        pass


def test_case_3():
    try:
        str_0 = 'Q@j9'
        list_0 = [str_0, str_0, str_0]
        var_0 = module_0.digitSum(list_0)
        assert var_0 == 0
        str_1 = ''
        var_1 = module_0.digitSum(str_1)
        assert var_1 == 0
        str_2 = 'Q+^nlma;M<^u"-it'
        var_2 = module_0.digitSum(str_2)
        assert var_2 == 158
        var_3 = module_0.digitSum(str_0)
        assert var_3 == 81
        bool_0 = False
        set_0 = {str_0, bool_0, str_2, var_3}
        var_4 = module_0.digitSum(set_0)
    except BaseException:
        pass
