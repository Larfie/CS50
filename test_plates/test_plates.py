from plates import is_valid


def main():
    test_is_valid1()
    test_is_valid2()
    test_is_valid3()
    test_is_valid4()
    test_is_valid5()
    test_is_valid6()
    test_is_valid7()
    test_is_valid8()
    test_is_valid9()
    test_is_valid10()
    test_is_valid11()
    test_is_valid12()


def test_is_valid1():
    assert is_valid("CS50") == True


def test_is_valid2():
    assert is_valid("CS05") == False


def test_is_valid3():
    assert is_valid("CS50P") == False


def test_is_valid4():
    assert is_valid("0000") == False


def test_is_valid5():
    assert is_valid("D D.") == False


def test_is_valid6():
    assert is_valid("CSPHARVARD50") == False


def test_is_valid7():
    assert is_valid("H") == False


def test_is_valid8():
    assert is_valid("PI3.14") == False


def test_is_valid9():
    assert is_valid("00PA") == False


def test_is_valid10():
    assert is_valid("..PA") == False


def test_is_valid11():
    assert is_valid("++PA") == False
    assert is_valid("_DEF") == False


def test_is_valid12():
    assert is_valid("PA") == True
    assert is_valid("2A") == False
    assert is_valid("A2") == False
    assert is_valid("22") == False





if __name__ == "__main__":
    main()