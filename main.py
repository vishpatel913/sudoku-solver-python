digits = '123456789'
rows = 'ABCDEFGHI'
cols = digits


def cross(A, B):
    "Cross product of elements in A and elements in B."
    # squares = []
    # for a in A:
    #     for b in B:
    #         squares.append(a+b)
    # return squares
    return [a+b for a in A for b in B]


squares = cross(rows, cols)

unitlist = ([cross(rows, c) for c in cols] +
            [cross(r, cols) for r in rows] +
            [cross(rs, cs) for rs in ('ABC', 'DEF', 'GHI') for cs in ('123', '456', '789')])

# units = {}
# for s in squares:
#     for u in unitlist:
#         if s in u:
#             if s not in units:
#                 units[s] = []
#             units[s].append(u)
units = dict((s, [u for u in unitlist if s in u]) for s in squares)

# peers = {}

# for s in squares:
#     unit_set = set()
#     for unit in units[s]:
#         for square in unit:
#             if square != s:
#                 unit_set.add(square)
#     peers[s] = unit_set
peers = dict((s, set(sum(units[s], [])) - set([s])) for s in squares)


def test():
    "A set of unit tests."
    assert len(squares) == 81
    assert len(unitlist) == 27
    assert all(len(units[s]) == 3 for s in squares)
    assert all(len(peers[s]) == 20 for s in squares)
    assert units['C2'] == [
        ['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2'],
        ['C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9'],
        ['A1', 'A2', 'A3', 'B1', 'B2', 'B3', 'C1', 'C2', 'C3']]
    assert peers['C2'] == set(
        ['A2', 'B2', 'D2', 'E2', 'F2', 'G2', 'H2', 'I2',
         'C1', 'C3', 'C4', 'C5', 'C6', 'C7', 'C8', 'C9',
         'A1', 'A3', 'B1', 'B3'])
    print('All tests pass.')


test()
