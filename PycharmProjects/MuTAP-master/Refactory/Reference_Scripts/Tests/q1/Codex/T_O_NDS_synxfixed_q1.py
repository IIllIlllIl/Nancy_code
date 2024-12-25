""" 
Takes in a value x and a sorted sequence seq, and returns the 
position that x should go to such that the sequence remains sorted. 
otherwise, return the length of the sequence
"""
def search(x, seq):
    for i in range(len(seq)):
        if x <= seq[i]:
            return i
    return len(seq)

def test():
    assert search(1, [1, 2]) == 0
    assert search(2, [1, 2]) == 1
    assert search(3, [1, 2]) == 1
    assert search(0, [1, 2]) == 0
    assert search(2, [1, 2]) == 1
    assert search(2, [1, 2, 3]) == 1
    assert search(3, [1, 2, 3]) == 2
    assert search(0, [1, 2, 3]) == 0
    assert search(4, [1, 2, 3]) == 3