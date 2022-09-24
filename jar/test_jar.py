from jar import Jar


def main():
    test_init()
    test_str()
    test_deposit()
    test_withdraw()


def test_init():
    jar = Jar()
    assert jar.capacity == 12

def test_str():
    jar = Jar()
    assert jar.__str__() == ""
    jar.deposit(1)
    assert jar.__str__() == "🍪"
    jar.deposit(2)
    assert jar.__str__() == "🍪🍪🍪"
    jar.deposit(9)
    assert jar.__str__() == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(2)
    assert jar.size == 2
    jar.deposit(3)
    assert jar.size == 5


def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(2)
    assert jar.size == 8
    jar.withdraw(5)
    assert jar.size == 3


if __name__=="__main__":
    main()