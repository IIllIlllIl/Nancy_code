def eat(number, need, remaining):
    
    if(need <= remaining):
        return [ number + need , remaining-need ]
    else:
        return [ number + remaining , 0]

def test():
    assert (eat(1, 1, 2) == [3, 0])
    
    
    assert (eat(1, 2, 2) == [3, 0])
    
    
     
    assert (eat(2, 3, 3) == [5, 0])
    
    
     
    assert (eat(2, 4, 4) == [6, 0])
    
    
     
    assert (eat(2, 5, 3) == [8, 1])
    
    
    assert 
    assert (eat(2, 3, 5) == [7, 2])
    
    
    assert 
    assert (eat(2, 6, 4) == [8, 2])
    
    
    assert 
    assert (eat(2, 7, 5) == [8, 2])
    
    