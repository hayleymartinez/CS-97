from doctest import testmod

def doubleAll(l):
    """Returns a list that is identical to l but with each value doubled.

    Arguments:
    l -- a list of integers
    """
    if l == []:
        return []
    else:
        return [l[0] * 2] + doubleAll(l[1:])


def countPos(l):
    """Returns the number of elements in l that are positive.

    Arguments:
    l -- a list of integers
    """
    if l == []:
        return 0
    else:
        if l[0] > 0:
            return 1 + countPos(l[1:])
        else:
            return countPos(l[1:])


def intRange(low, high):
    """Returns a list of integers in the range low to high, inclusive.

    Arguments:
    low -- the lower bound (an integer)
    high -- the upper bound (an integer)
    """
    if low == high:
        return [high]
    else:
        return [low] + intRange(low + 1, high)


def merge(l1, l2):
    """Merge two sorted integer lists to produce a new sorted
    list of their elements.

    Arguments:
    l1 -- the first list
    l2 -- the second list
    """
    if l1 == []:
        if l2 == []:
            return l1
        else:
            return l2
    elif l2 == []:
        return l1
    else:
        if l1[0] < l2[0]:
            return [l1[0]] + [l2[0]] + merge(l1[1:],l2[1:])
        else:
            return [l2[0]] + [l1[0]] + merge(l1[1:], l2[1:])


# run all doctests whenever this file is run (via the Run menu in IDLE)
if __name__ == '__main__':
    testmod()

