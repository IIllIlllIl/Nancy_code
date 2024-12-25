def any_int(x, y, z):
  
    
    if isinstance(x,int) and isinstance(y,int) and isinstance(z,int):
        if (x+y==z) or (x+z==y) or (y+z==x):
            return True
        return False
    return False

def test():
   assert any_int(1, 2, 3) == True
    assert any_int(1, 2, 4) == False
    assert any_int(1, 2, 5) == False
    assert any_int(1, 2, 6) == False
    assert any_int(1, 2, 7) == False
    assert any_int(1, 2, 8) == False
    assert any_int(1, 2, 9) == False
    assert any_int(1, 2, 10) == False
    assert any_int(1, 2, 11) == False
    assert any_int(1, 2, 12) == False
    assert any_int(1, 2, 13) == False
    assert any_int(1, 