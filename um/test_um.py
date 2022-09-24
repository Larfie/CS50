from um import count

def test_count_one():
    assert count("um?") == 1
    assert count("um ummi") == 1
    assert count("UM") == 1
    assert count("Um") == 1


def test_count_zero():
    assert count("ummm") == 0
    assert count("umumumum") == 0
    assert count("") == 0
    assert count("13") == 0

def test_count_more():
    assert count("Um um, UM") == 3
    assert count("#2 um! ola um, UM. no more ums") == 3
    
