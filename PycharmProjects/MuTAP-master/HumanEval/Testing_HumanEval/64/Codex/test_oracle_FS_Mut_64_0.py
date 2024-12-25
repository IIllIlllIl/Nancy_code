def vowels_count(s):
    
    vowels = "aeiouAEIOU"
    n_vowels = sum(c in vowels for c in s)
    if s[-1] == 'y' or s[-1] == 'Y':
        n_vowels += 1
    return n_vowels



def test():
    assert vowels_count("ac") == 1
    assert vowels_count("ac") == 1
    assert vowels_count("") == 0

