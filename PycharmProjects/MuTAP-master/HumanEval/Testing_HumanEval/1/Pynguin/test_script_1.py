# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import script_1 as module_0


def test_case_0():
    str_0 = "Sf-n g{faXj"
    list_0 = module_0.separate_paren_groups(str_0)


def test_case_1():
    str_0 = 'ucA %L"XId8sdV'
    list_0 = module_0.separate_paren_groups(str_0)
    list_1 = module_0.separate_paren_groups(str_0)
    str_1 = "9F$?L)'cUcSG"
    list_2 = module_0.separate_paren_groups(str_0)
    list_3 = module_0.separate_paren_groups(str_1)
    str_2 = ":MU9(\t=_9v"
    list_4 = module_0.separate_paren_groups(str_2)
    list_5 = module_0.separate_paren_groups(str_2)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = ")H"
    list_0 = module_0.separate_paren_groups(str_0)
    list_1 = module_0.separate_paren_groups(str_0)
    none_type_0 = None
    module_0.separate_paren_groups(none_type_0)


def test_case_3():
    str_0 = "g<)\n6:v|<\x0c#|"
    str_1 = "@\t~+JGvz"
    list_0 = module_0.separate_paren_groups(str_1)
    list_1 = module_0.separate_paren_groups(str_0)
    str_2 = "fa Wx6[?qGtD\x0bqmio"
    str_3 = "k@>fn0:Oi\x0c+k"
    list_2 = module_0.separate_paren_groups(str_2)
    list_3 = module_0.separate_paren_groups(str_3)
    str_4 = "s-I(BWKA)gw\ts.**/:D"
    list_4 = module_0.separate_paren_groups(str_4)
