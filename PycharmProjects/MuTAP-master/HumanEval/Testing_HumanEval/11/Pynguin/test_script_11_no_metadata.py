# Automatically generated by Pynguin.
import script_11 as module_0


def test_case_0():
    str_0 = 'b:g'
    str_1 = module_0.string_xor(str_0, str_0)
    assert str_1 == '000'



def test_case_1():
    str_0 = '?RW`'
    str_1 = 'S)VNJsnS:0,"~u|#'
    str_2 = module_0.string_xor(str_0, str_1)
    assert str_2 == '1111'

