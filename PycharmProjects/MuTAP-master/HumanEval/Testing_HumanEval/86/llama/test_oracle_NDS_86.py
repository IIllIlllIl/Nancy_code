def anti_shuffle(s):
    
    return ' '.join([''.join(sorted(list(i))) for i in s.split(' ')])


# test case
def test():
    # Test with a small string
    assert anti_shuffle("Hello World") == "Hll wrld"
    # Test with a medium-sized string
    assert anti_shuffle("The quick brown fox jumps over the lazy dog") == "Thq buor fnx jmpsvr th lzy dg"
    # Test with a long string
    assert anti_shuffle("The quick brown fox jumps over the lazy dog with excitement and joy") == "Thq buor fnx jmpsvr th lzy dg wth xctd and jy"
    # Test with multiple spaces in a word
    assert anti_shuffle("The quick brown fox jumps over the lazy dog with a big smile on his face") == "Thq buor fnx jmpsvr th lzy dg wth bbig sml on hs fce"
    # Test with a string containing numbers
    assert anti_shuffle("1234567