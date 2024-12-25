from typing import List
#<code> 
def triangle(x: int, y: int, z: int) -> str:
    if x == y == z:
        return "Equilateral triangle"
    elif x == y or y == z or x == z:
        return "Isosceles triangle"
    else:
        return "Scalene triangle"
#</code>
#<test>
def test_equilateral_triangle():
    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"
#</test>
#<code>
def has_close_elements(numbers: List[float], threshold: float) -> bool:
    for idx, elem in enumerate(numbers):
        for idx2, elem2 in enumerate(numbers):
            if idx != idx2:
                distance = abs(elem - elem2)
                if distance < threshold:
                    return True

    return False
#</code>
#<test>
def check(candidate):
    assert candidate([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) == True
    assert candidate([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.05) == False
    assert candidate([1.0, 2.0, 5.9, 4.0, 5.0], 0.95) == True
    assert candidate([1.0, 2.0, 5.9, 4.0, 5.0], 0.8) == False
    assert candidate([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.1) == True
#</test>
#<code>
def get_positive(l: list):
    """Return only positive numbers in the list.
    """
    return [e for e in l if e > 0]


METADATA = {}



#</code>
#<test>

def test_get_positive():
    assert get_positive([]) == []
    assert get_positive([1, 2, 3]) == [1, 2, 3]
    assert get_positive([-1, -2, -3]) == []
    assert get_positive([1, -2, -3]) == [1]
    assert get_positive([-1, 2, -3]) == [2]
    assert get_positive([-1, -2, 3]) == [3]
    assert get_positive([1, 2, -3]) == [1, 2]
    assert get_positive([-1, 2, 3]) == [2, 3]
    assert get_positive([1, -2, 3]) == [1, 3]


