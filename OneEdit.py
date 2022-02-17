"""
Function that determines if more than one edit is needed between two strings.
An edit can be the addition, deletion, or change of a character.
Args:
    param1: The first input string
    param2: The second input string
Returns:
    Returns true if only 1 edit is needed between strings. Returns false otherwise.
"""


def oneEdit(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    edits = 0
    p1 = 0
    p2 = 0

    if abs(l1 - l2) > 1:
        return False

    while p1 < l1 and p2 < l2:
        if s1[p1] != s2[p2]:
            edits += 1
            if edits > 1:
                return False
            if l1 < l2:
                p2 += 1
            else:
                p1 += 1
                p2 += 1

        else:
            p1 += 1
            p2 += 1
    if p1 < l1 or p2 < l2:
        edits += 1

    return edits == 1


if __name__ == '__main__':
    a = "edit"
    b = "edit1"
    c = "edit 2"
    result1 = oneEdit(a, b)
    result2 = oneEdit(a, c)
    print(result1)
    print(result2)
