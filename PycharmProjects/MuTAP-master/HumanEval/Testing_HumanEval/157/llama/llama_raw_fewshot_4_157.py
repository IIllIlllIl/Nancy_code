[INST] <<SYS>>
You are a python coding assistant. Always answer with python code.
<</SYS>>

Generate a test function that includes different tests in the form of one line assertion [/INST] These are examples of code and test case function:

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

def test():
    assert triangle(2, 2, 2) == "Equilateral triangle"
    assert triangle(2, 2, 3) == "Isosceles triangle"
    assert triangle(2, 3, 4) == "Scalene triangle"
#</test>

#<code>

from typing import List
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

def test():
    assert has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.3) == True
    assert has_close_elements([1.0, 2.0, 3.9, 4.0, 5.0, 2.2], 0.05) == False
    assert has_close_elements([1.0, 2.0, 5.9, 4.0, 5.0], 0.95) == True
    assert has_close_elements([1.0, 2.0, 5.9, 4.0, 5.0], 0.8) == False
    assert has_close_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0], 0.1) == True
#</test>  [INST] Based on the examples of function code and their test function, generate test cases for the following function:
#<code>
def right_angle_triangle(a, b, c):
    '''
    Given the lengths of the three sides of a triangle. Return True if the three
    sides form a right-angled triangle, False otherwise.
    A right-angled triangle is a triangle in which one angle is right angle or 
    90 degree.
    Example:
    right_angle_triangle(3, 4, 5) == True
    right_angle_triangle(1, 2, 3) == False
    '''
    return a*a == b*b + c*c or b*b == a*a + c*c or c*c == a*a + b*b


#</code>
#<test>
def test():
    assert [/INST]  Definitely! Here are some test cases for the `right_angle_triangle` function:

#<test>

def test():
    assert right_angle_triangle(3, 4, 5) == True
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(4, 5, 6) == False
    assert right_angle_triangle(6, 8, 10) == False
    assert right_angle_triangle(3, 4, 6) == False
    assert right_angle_triangle(1, 2, 3) == False
#</test>

#<code>

def test():
    a = float(input("Enter side length a: "))
    b = float(input("Enter side length b: "))
    c = float(input("Enter side length c: "))
    if right_angle_triangle(a, b, c):
        print("The triangle is a right-angled triangle!")
    else:
        print("The triangle is not a right-angled triangle.")