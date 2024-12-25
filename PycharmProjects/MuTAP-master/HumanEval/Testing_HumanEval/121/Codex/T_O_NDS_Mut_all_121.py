def solution(lst):
    
    return sum([x for idx, x in enumerate(lst) if idx%2==0 and x%2==1])



def test():

    assert solution([1, 0, 1, 1, 0, 1, 0]) == 2
    assert solution([]) == 0
    assert solution([1, 0, 1, 1, 0, 1, 0]) == 2
    assert solution([0, 1, 1, 0]) == 1
    assert solution([0, 0, 0]) == 3
    assert solution([0, 1, 2, 3, 0, 1, 2, 3, 2, 3, 2, 0]) == 1
    assert solution([]) == 0

