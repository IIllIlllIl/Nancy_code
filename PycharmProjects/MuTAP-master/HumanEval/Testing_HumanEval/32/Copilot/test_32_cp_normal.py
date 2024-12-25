from script_32_cp_normal import find_zero

def generate_test_case():
    assert find_zero([1, 0, -1]) == 1
    assert find_zero([1, 0, -4]) == 2
    assert find_zero([1, 0, 0, -1]) == 1
    assert find_zero([1, 0, 0, -8]) == 2
    assert find_zero([1, 0, 0, 0, -1]) == 1
    assert find_zero([1, 0, 0, 0, -16]) == 2
    assert find_zero([1, 0, 0, 0, 0, -1]) == 1
    assert find_zero([1, 0, 0, 0, 0, -32]) == 2
    assert find_zero([1, 0, 0, 0, 0, 0, -1]) == 1
    assert find_zero([1, 0, 0, 0, 0, 0, -64]) == 2
    assert find_zero([1, 0, 0, 0, 0, 0, 0, -1]) == 1
    assert find_zero([1, 0, 0, 0, 0, 0, 0, -128]) == 2
    assert find_zero([1, 0, 0, 0, 0, 0, 0, 0, -1]) == 1
    assert find_zero([1, 0, 0, 0, 0, 0, 0, 0, -256]) == 2
    assert find_zero([1, 0, 0, 0, 0, 0, 0, 0, 0, -1]) == 1
    assert find_zero([1, 0, 0, 0, 0, 0, 0, 0, 0, -512]) == 2
    assert find_zero([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1]) == 1