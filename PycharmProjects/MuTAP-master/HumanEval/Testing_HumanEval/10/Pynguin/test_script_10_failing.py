# Automatically generated by Pynguin.
import script_10 as module_0


def test_case_0():
    try:
        str_0 = None
        str_1 = '1A\n+'
        str_2 = module_0.make_palindrome(str_1)
        assert str_2 == '1A\n+\nA1'
        bool_0 = module_0.is_palindrome(str_0)
    except BaseException:
        pass


def test_case_1():
    try:
        str_0 = 'U2BY(D\\A^c\th'
        bool_0 = module_0.is_palindrome(str_0)
        assert bool_0 is False
        str_1 = None
        str_2 = module_0.make_palindrome(str_1)
        assert str_2 == ''
        str_3 = 'QkB(u3dNh1Po'
        str_4 = module_0.make_palindrome(str_3)
        assert str_4 == 'QkB(u3dNh1PoP1hNd3u(BkQ'
        bool_1 = module_0.is_palindrome(str_1)
    except BaseException:
        pass