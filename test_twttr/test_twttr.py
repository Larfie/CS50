from twttr import shorten

def main():
    test_shorten()


def test_shorten1():
    assert shorten("twitter") == "twttr"


def test_shorten2():
    assert shorten("45rtTa") == "45rtT"


def test_shorten3():
    assert shorten("...") == "..."

def test_shorten4():
    assert shorten("AeIoU RRRd") == " RRRd"


if __name__ == "__main__":
    main()
