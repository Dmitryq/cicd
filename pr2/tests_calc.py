from calc import add

def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_add2():
    assert add(2, 2) == 4
    assert add(-1, 0) == -1
    assert add(3, 3) == 6
