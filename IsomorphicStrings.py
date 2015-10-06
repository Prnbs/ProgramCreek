__author__ = 'psinha4'


def test_isomorphic(str1, str2):
    if len(str1) != len(str2):
        return False
    if len(str1) == 0 and len(str2) == 0:
        return True
    str1 = str1.replace(str1[0], "")
    str2 = str2.replace(str2[0], "")
    return test_isomorphic(str1, str2)


if __name__ == '__main__':
    str1 = "abca"
    str2 = "opqo"
    print test_isomorphic(str1, str2)