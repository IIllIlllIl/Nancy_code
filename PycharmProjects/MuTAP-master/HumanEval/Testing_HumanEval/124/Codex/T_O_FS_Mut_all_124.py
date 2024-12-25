def valid_date(date):
    
    try:
        date = date.strip()
        month, day, year = date.split('-')
        month, day, year = int(month), int(day), int(year)
        if month < 1 or month > 12:
            return False
        if month in [1,3,5,7,8,10,12] and day < 1 or day > 31:
            return False
        if month in [4,6,9,11] and day < 1 or day > 30:
            return False
        if month == 2 and day < 1 or day > 29:
            return False
    except:
        return False

    return True



def test():
    assert valid_date("4-4-2004") == True
    assert valid_date("2-30-2000") == False
    assert valid_date("30-2-2000") == False
    assert valid_date("1-1-2001") == True
    assert valid_date("4-4-2004") == True
    assert valid_date('4-4-2004') == True
    assert valid_date('12-4-2004') == False
    assert valid_date('4-30-2004') == False
    assert valid_date("4-4-2004") == False
    assert valid_date("4-44-2004") == False
    assert valid_date("2-2-2004") == True
    assert valid_date("4-4-2004") == True
    assert valid_date("4-4-2004") == False
    assert valid_date("2-32-2014") == False
    assert valid_date("1-1-2013") == True
    assert valid_date("1-1-2013") == True
    assert valid_date("") == True
    assert valid_date("29-2-2013") == True
    assert valid_date("2-2-2012") == True
    assert valid_date("4-4-2004") == True
    assert valid_date("4-4-2004") == True

