from watch import parse


def main():
    test_parse1()


def test_parse1():
    assert parse(r'<iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>') == "https://youtu.be/xvFZjo5PgG0"
    assert parse(r'<iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>') == "https://youtu.be/xvFZjo5PgG0"
    assert parse(r'<iframe width="560" height="315" src="https://cs50.harvard.edu/python"></iframe>') == None



if __name__ == "__main__":
    main()