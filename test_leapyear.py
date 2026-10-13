from leap import leapyear

def test_year1():
    assert leapyear(2020) == True

def test_year2():
    assert leapyear(2021) == False

def test_year3():
    assert leapyear(1900) == False

def test_year4():
    assert leapyear(2000) == True