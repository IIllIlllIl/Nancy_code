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
    assert valid_date('') == False
    assert valid_date('2020-02-30') == False
    assert valid_date('2020-01-30') == False
    assert valid_date('2019-02-30') == False
    assert valid_date('2020-02-29') == False
    assert valid_date('2020-02-28') == False
    assert valid_date('2020-02-29') == False
    assert valid_date('2020-02-29') == False
    assert valid_date('2020-02-29') == False
    assert valid_date('2020-02-29') == False
