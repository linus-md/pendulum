from core.parse import parse

def test_parse():
    log = '[65535:4]2(3)s(2)sss3(3)s(4)s(5)s(7)s4(9)s(11)--s(12)s(15)----5---s(10)s(11)s(14)-----6--------'
    vals, _ = parse(log)
    assert vals == [[2, 4, 0], [3, 4, 0], [4, 3, 6], [5, 3, 8], [6, 0, 8]]